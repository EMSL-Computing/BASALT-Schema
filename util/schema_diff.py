"""Detect breaking changes between two versions of the BASALT schema.

Compares the schema at a git ref (the "base", e.g. the last tag or the MR's
merge-base) against the working tree (or a second ref) and reports changes
that would break downstream consumers:

  * classes, slots or enums removed (with a "possible rename" hint when a
    similar element was added, or when the new element declares the old name
    in ``aliases``)
  * a slot removed from a class's induced (inherited + own) slot set
  * a slot's ``range``, ``multivalued`` or ``identifier`` changed on a class
  * a slot newly ``required`` on a class
  * a class newly ``abstract``
  * permissible values removed from an enum

Additions and relaxations (e.g. required -> optional) are listed as info.

Usage:
  python util/schema_diff.py --base v0.2.0
  python util/schema_diff.py --base origin/dev --head HEAD --output report.md --fail-on-breaking

Exit code is 1 when ``--fail-on-breaking`` is set and breaking changes exist.
"""

from __future__ import annotations

import argparse
import difflib
import subprocess
import sys
import tarfile
import tempfile
from collections import defaultdict
from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path

from linkml_runtime import SchemaView

SCHEMA_DIR = "src/basalt_schema/schema"
SCHEMA_FILE = "basalt_schema.yaml"
RENAME_SIMILARITY = 0.75


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #


def extract_ref(ref: str, dest: Path) -> Path:
    """Extract SCHEMA_DIR at a git ref into dest; return the root schema path."""
    archive = subprocess.run(
        ["git", "archive", "--format=tar", ref, SCHEMA_DIR],
        check=True,
        capture_output=True,
    ).stdout
    with tarfile.open(fileobj=BytesIO(archive)) as tar:
        tar.extractall(dest, filter="data")
    root = dest / SCHEMA_DIR / SCHEMA_FILE
    if not root.exists():
        sys.exit(f"{SCHEMA_FILE} not found in {SCHEMA_DIR} at ref {ref!r}")
    return root


def load(ref: str | None, tmp: Path) -> SchemaView:
    path = extract_ref(ref, tmp / "ref") if ref else Path(SCHEMA_DIR) / SCHEMA_FILE
    return SchemaView(str(path))


# --------------------------------------------------------------------------- #
# Comparison
# --------------------------------------------------------------------------- #


@dataclass
class Report:
    breaking: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)


def _range(slot) -> str:
    """Normalised range string, folding any_of ranges in."""
    ranges = sorted({x.range for x in (slot.any_of or []) if x.range})
    if ranges:
        return " | ".join(ranges)
    return slot.range or ""


def _rename_hint(old: str, added: set[str], aliases: dict[str, set[str]]) -> str:
    declared = [new for new in added if old in aliases.get(new, set())]
    if declared:
        return f" (renamed to `{declared[0]}` via `aliases`)"
    close = difflib.get_close_matches(old, list(added), n=1, cutoff=RENAME_SIMILARITY)
    return f" (possible rename to `{close[0]}`?)" if close else ""


def _aliases(elements) -> dict[str, set[str]]:
    return {name: set(el.aliases or []) for name, el in elements.items()}


def _added_removed(base: dict, head: dict, kind: str, report: Report) -> None:
    removed = sorted(set(base) - set(head))
    added = set(head) - set(base)
    aliases = _aliases(head)
    for name in removed:
        report.breaking.append(f"{kind} `{name}` removed{_rename_hint(name, added, aliases)}")
    if added:
        plural = "Classes" if kind == "Class" else f"{kind}s"
        report.info.append(f"{plural} added: " + ", ".join(f"`{n}`" for n in sorted(added)))


def _fmt_classes(classes: list[str], limit: int = 6) -> str:
    shown = ", ".join(f"`{c}`" for c in classes[:limit])
    more = len(classes) - limit
    return shown + (f" and {more} more" if more > 0 else "")


def compare(base: SchemaView, head: SchemaView) -> Report:
    report = Report()
    b_classes, h_classes = base.all_classes(), head.all_classes()
    b_slots, h_slots = base.all_slots(), head.all_slots()
    b_enums, h_enums = base.all_enums(), head.all_enums()

    _added_removed(b_classes, h_classes, "Class", report)
    _added_removed(b_slots, h_slots, "Slot", report)
    _added_removed(b_enums, h_enums, "Enum", report)

    # Per-class induced slots. Changes are grouped by (slot, change) so a
    # change to a shared slot is reported once with the classes it affects.
    breaking: dict[str, list[str]] = defaultdict(list)
    info: dict[str, list[str]] = defaultdict(list)
    for cname in sorted(set(b_classes) & set(h_classes)):
        if not b_classes[cname].abstract and h_classes[cname].abstract:
            report.breaking.append(f"Class `{cname}` is now `abstract`")

        b_ind = {s.name: s for s in base.class_induced_slots(cname)}
        h_ind = {s.name: s for s in head.class_induced_slots(cname)}

        for sname in sorted(set(b_ind) - set(h_ind)):
            # Globally-removed slots are already reported above.
            if sname in h_slots:
                breaking[f"Slot `{sname}` removed from class"].append(cname)
        for sname in sorted(set(h_ind) - set(b_ind)):
            if h_ind[sname].required:
                breaking[f"New required slot `{sname}` added to class"].append(cname)

        for sname in sorted(set(b_ind) & set(h_ind)):
            old, new = b_ind[sname], h_ind[sname]
            if _range(old) != _range(new):
                breaking[f"Slot `{sname}` range changed `{_range(old)}` → `{_range(new)}`"].append(cname)
            if bool(old.required) != bool(new.required):
                key = f"Slot `{sname}` required {bool(old.required)} → {bool(new.required)}"
                (breaking if new.required else info)[key].append(cname)
            if bool(old.multivalued) != bool(new.multivalued):
                breaking[f"Slot `{sname}` multivalued {bool(old.multivalued)} → {bool(new.multivalued)}"].append(cname)
            if bool(old.identifier) != bool(new.identifier):
                breaking[f"Slot `{sname}` identifier {bool(old.identifier)} → {bool(new.identifier)}"].append(cname)

    report.breaking += [f"{k} on {_fmt_classes(v)}" for k, v in breaking.items()]
    report.info += [f"{k} on {_fmt_classes(v)}" for k, v in info.items()]

    # Enum permissible values
    for ename in sorted(set(b_enums) & set(h_enums)):
        b_pv = set(b_enums[ename].permissible_values or {})
        h_pv = set(h_enums[ename].permissible_values or {})
        if gone := sorted(b_pv - h_pv):
            report.breaking.append(
                f"Enum `{ename}` lost permissible value(s): " + ", ".join(f"`{v}`" for v in gone)
            )
        if new := sorted(h_pv - b_pv):
            report.info.append(f"Enum `{ename}` gained value(s): " + ", ".join(f"`{v}`" for v in new))

    return report


# --------------------------------------------------------------------------- #
# Output
# --------------------------------------------------------------------------- #


def to_markdown(report: Report, title: str) -> str:
    lines = [f"### {title}", ""]
    if report.breaking:
        lines.append(f"**{len(report.breaking)} breaking change(s)**")
        lines += [f"- {x}" for x in report.breaking]
    else:
        lines.append("No breaking changes.")
    if report.info:
        lines += ["", "<details><summary>Non-breaking changes "
                  f"({len(report.info)})</summary>", ""]
        lines += [f"- {x}" for x in report.info]
        lines += ["", "</details>"]
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base", required=True, help="git ref to compare against (e.g. v0.2.0)")
    p.add_argument("--head", default=None, help="git ref to compare (default: working tree)")
    p.add_argument("--title", default=None, help="heading for the markdown report")
    p.add_argument("--output", type=Path, help="write markdown report here (default: stdout)")
    p.add_argument("--fail-on-breaking", action="store_true", help="exit 1 if breaking changes found")
    args = p.parse_args()

    with tempfile.TemporaryDirectory() as b_tmp, tempfile.TemporaryDirectory() as h_tmp:
        base = load(args.base, Path(b_tmp))
        head = load(args.head, Path(h_tmp))
        report = compare(base, head)

    title = args.title or f"Schema changes vs `{args.base}`"
    md = to_markdown(report, title)
    if args.output:
        args.output.write_text(md, encoding="utf-8")
    else:
        sys.stdout.write(md)
    return 1 if (args.fail_on_breaking and report.breaking) else 0


if __name__ == "__main__":
    sys.exit(main())
