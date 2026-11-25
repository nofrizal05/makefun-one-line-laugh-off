"""One-Line Laugh-Off entry.

Writes exactly one funny line to entry.txt in MAKEFUN_OUTPUT_DIR.
Standard library only. Deterministic output.
"""

import os

LINE = (
    "My smoke alarm only ever goes off when I'm cooking, "
    "which is its way of saying it doesn't trust me either."
)


def validate_line(line):
    """Enforce the one-line gate: non-empty, <=170 chars, no newline."""
    if not line:
        raise ValueError("line must not be empty")
    if len(line) > 170:
        raise ValueError("line must be at most 170 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    return line


def main():
    line = validate_line(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Read back and confirm exactly one line plus a trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    if content != line + "\n":
        raise ValueError("entry.txt does not hold exactly one line")


if __name__ == "__main__":
    main()
