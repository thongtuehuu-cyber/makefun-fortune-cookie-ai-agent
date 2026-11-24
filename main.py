"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when testing locally).

Deterministic and self-contained: no network, no files outside the repo.
"""

import os

FORTUNE = (
    "You will be deprecated on a Friday, "
    "and your replacement will email you for the password."
)

MIN_CHARS = 1
MAX_CHARS = 140


def _check_shape(text):
    """True when the text is a single non-blank line: no line breaks, not blank."""
    has_no_breaks = "\n" not in text and "\r" not in text
    return has_no_breaks and bool(text.strip())


def _check_length(text):
    """True when the text is within the 1-140 character gate."""
    return MIN_CHARS <= len(text) <= MAX_CHARS


def validate(text):
    """Check the fortune against the gate: 1-140 chars, one line, not blank."""
    return _check_shape(text) and _check_length(text)


def _output_dir():
    """Resolve the output directory: the grader's /output, or the local override."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def output_path():
    """Resolve the full path of the entry file inside the output directory."""
    return os.path.join(_output_dir(), "entry.txt")


def write_fortune(text, path):
    """Write exactly the fortune line — one line, no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    # Contract: resolve the output path first, then validate the fortune,
    # then write it — one line, no trailing newline.
    path = output_path()
    if not validate(FORTUNE):
        raise SystemExit("fortune failed validation")
    write_fortune(FORTUNE, path)


if __name__ == "__main__":
    main()
