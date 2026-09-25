"""Remove the wall-clock timestamp from LinkML-generated Python.

``pythongen`` stamps a ``# Generation date: <ISO timestamp>`` line into the
header of the generated dataclass module. That single line makes every
``just gen-project`` produce a diff even when the schema is unchanged, which
buries real modeling changes in review. We rewrite the value to a fixed
placeholder so the generated artifact is byte-stable for identical input.

Usage: python util/strip_gen_timestamp.py <file> [<file> ...]
"""

import re
import sys
from pathlib import Path

PATTERN = re.compile(r"^(# Generation date: ).*$", re.MULTILINE)
PLACEHOLDER = r"\1(not recorded - see git history)"


def normalize(path: Path) -> bool:
    """Rewrite ``path`` in place. Returns True if the file changed."""
    original = path.read_text(encoding="utf-8")
    updated = PATTERN.sub(PLACEHOLDER, original)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        return 2
    for arg in argv:
        path = Path(arg)
        if not path.is_file():
            continue
        if normalize(path):
            print(f"normalized generation date in {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
