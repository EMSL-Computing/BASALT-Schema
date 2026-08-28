"""
util/gen_doc.py
===============
Custom gen-doc entry point for basalt-schema.

Why this exists
---------------
The stock `gen-doc` tool creates a Jinja2 environment with a single
FileSystemLoader pointed at ONE directory.  When a custom --template-directory
is provided, its loader replaces the installed-template loader entirely.
Any {% include %} calls inside a top-level template therefore resolve from
the SAME single folder, so an override of 'class_diagram.md.jinja2' is
invisible when 'class.md.jinja2' is loaded from the installed dir.

This script monkey-patches DocGenerator._get_template to use a
ChoiceLoader (custom dir → installed dir), giving proper template
inheritance without needing to copy the full template tree.

It also patches DocGenerator.link, which has a latent bug: it guards
against a None input but not against get_element() returning None for
schema-opaque types (uuid, numeric).  Those types are intentionally
undefined in the operational schema and resolved by the API at runtime.

Usage
-----
    uv run python util/gen_doc.py                       # uses defaults
    uv run python util/gen_doc.py <schema> <out_dir>    # explicit args

Or via justfile:
    just gen-doc
"""

import importlib.util
import os
import sys
import types

from jinja2 import ChoiceLoader, Environment, FileSystemLoader
from linkml.generators.docgen import DocGenerator, customize_environment

# ---------------------------------------------------------------------------
# Defaults (relative to repo root)
# ---------------------------------------------------------------------------
DEFAULT_SCHEMA = "src/basalt_schema/schema/basalt_schema.yaml"
DEFAULT_OUT_DIR = "docs/elements/"
CUSTOM_TEMPLATES = "src/doc_templates/"


def _build_patched_get_template(custom_dir: str, installed_dir: str):
    """Return a replacement _get_template method using a ChoiceLoader."""

    def _get_template(self, element_type: str):
        base_file_name = f"{element_type}.{self._file_suffix()}.jinja2"
        loader = ChoiceLoader(
            [
                FileSystemLoader(custom_dir),
                FileSystemLoader(installed_dir),
            ]
        )
        env = Environment(loader=loader)
        customize_environment(env)
        return env.get_template(base_file_name)

    return _get_template


def _build_patched_link(original_link):
    """
    Return a patched `link` method that handles the case where
    schemaview.get_element() returns None for opaque types like
    `uuid` and `numeric` that are intentionally undefined in the schema.
    The stock link() guards against a None *input* but not against
    get_element() returning None for unresolved range names.
    """

    def link(self, *args, **kwargs):
        # First positional arg is the element/name being linked
        e = args[0] if args else kwargs.get("e")
        if isinstance(e, str):
            resolved = self.schemaview.get_element(e)
            if resolved is None:
                return e  # render opaque type name as plain text, no link
        return original_link(self, *args, **kwargs)

    return link


def main() -> None:
    schema = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCHEMA
    out_dir = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT_DIR

    # Resolve the installed docgen template directory
    spec = importlib.util.find_spec("linkml.generators.docgen")
    installed_templates = os.path.join(os.path.dirname(spec.origin), "docgen", "")

    gen = DocGenerator(schema, directory=out_dir)

    # Patch 1: ChoiceLoader so custom templates shadow the installed ones
    patched_get_template = _build_patched_get_template(CUSTOM_TEMPLATES, installed_templates)
    gen._get_template = types.MethodType(patched_get_template, gen)

    # Patch 2: guard link() against get_element() returning None for
    # opaque types (uuid, numeric) that are undefined in the schema
    original_link_func = DocGenerator.link
    gen.link = types.MethodType(_build_patched_link(original_link_func), gen)

    gen.serialize()
    print(f"Documentation written to {out_dir}")


if __name__ == "__main__":
    main()
