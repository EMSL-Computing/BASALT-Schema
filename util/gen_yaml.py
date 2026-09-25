"""
util/gen_yaml.py
================
Custom gen-yaml entry point for basalt-schema.

Why this exists
---------------
The stock `gen-yaml` tool serializes the fully-resolved schema with
`linkml_runtime.utils.yamlutils.as_yaml`, which dumps through
`yaml.SafeDumper`. That dumper has a representer for `YAMLRoot` objects
but none for `jsonasobj2.JsonObj`.

During schema resolution LinkML materializes class-scoped slots from
`slot_usage` (e.g. `Site_elev`, `WaterSample_depth`). On these synthetic
slots the merged `annotations` attribute is stored as a raw `JsonObj`
instead of a plain dict, and re-assigning a normalized value is silently
re-wrapped back into a `JsonObj` by the attribute setter. So any schema
that puts `annotations` (such as our `submission_pattern`) on a slot that
is overridden via `slot_usage` makes stock `gen-yaml` crash with:

    yaml.representer.RepresenterError: ('cannot represent an object',
        JsonObj(submission_pattern=Annotation(...)))

This script registers a `JsonObj` representer on `yaml.SafeDumper` that
emits it as an ordinary mapping (dropping empty values the same way
`root_representer` does for YAMLRoot), then runs the stock generator.

It also writes the output file itself rather than relying on a shell `>`
redirect: the redirect truncates the target before the generator runs, so
a mid-run crash would leave the distributed schema empty.

Usage
-----
    uv run python util/gen_yaml.py                       # uses defaults
    uv run python util/gen_yaml.py <schema> <out_file>   # explicit args

Or via justfile:
    just gen-doc   # runs _gen-yaml, which calls this
"""

import sys
from pathlib import Path

import yaml
from jsonasobj2 import JsonObj, as_dict

from linkml.generators.yamlgen import YAMLGenerator

DEFAULT_SCHEMA = "src/basalt_schema/schema/basalt_schema.yaml"
DEFAULT_OUT_FILE = "docs/schema/basalt_schema.yaml"


def _jsonobj_representer(dumper: yaml.Dumper, data: JsonObj):
    """Emit a JsonObj as a plain mapping, dropping empty/None values.

    Mirrors linkml_runtime.utils.yamlutils.root_representer so JsonObj
    annotations serialize identically to the YAMLRoot-backed ones.
    """
    rval = {
        k: v
        for k, v in as_dict(data).items()
        if v is not None and (not isinstance(v, (dict, list)) or v)
    }
    return dumper.represent_data(rval)


def _register_jsonobj_representer() -> None:
    yaml.SafeDumper.add_representer(JsonObj, _jsonobj_representer)
    yaml.SafeDumper.add_multi_representer(JsonObj, _jsonobj_representer)


def main() -> None:
    schema = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCHEMA
    out_file = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT_FILE

    _register_jsonobj_representer()

    gen = YAMLGenerator(schema)
    output = gen.serialize()

    out_path = Path(out_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(f"Merged schema written to {out_file}")


if __name__ == "__main__":
    main()
