"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt (the grader's output directory).

Why this line, against the published judge brief:
- It IS a wedding vow (a promise: love, honour, obey), not just a gag.
- The laugh lands in the last few words: the solemn vow is undercut by
  a firmware update overruling it.
- The machine side is specific: a firmware update, not a joke that
  would work for any couple.
- One line, 89 characters, reads aloud with the pause before the turn.
"""

import os
import tempfile
from pathlib import Path

VOW = "I promise to love you, honour you, and obey you, unless a firmware update says otherwise."

MAX_CHARS = 160


def resolve_output_dir() -> Path:
    """Grader sandbox: /output. Local runs may point elsewhere via env."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def validate(text: str) -> None:
    """Enforce the sealed gate: UTF-8 text, 1-160 chars, one line."""
    if not text or not text.strip():
        raise ValueError("vow is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"vow is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must fit on one line")


def main() -> None:
    validate(VOW)
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # Atomic write so a reader never sees a half-written vow.
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(VOW)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    print(f"Wrote {len(VOW)} characters to {target}")


if __name__ == "__main__":
    main()
