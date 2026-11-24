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


def _is_single_line(text):
    """True when the text holds no line breaks at all."""
    return "\n" not in text and "\r" not in text


def _is_within_length(text):
    """True when the text is within the 1-140 character gate."""
    return MIN_CHARS <= len(text) <= MAX_CHARS


def _is_not_blank(text):
    """True when the text holds more than whitespace."""
    return bool(text.strip())


def validate(text):
    """Check the fortune against the gate: 1-140 chars, one line, not blank."""
    checks = (_is_single_line(text), _is_within_length(text), _is_not_blank(text))
    return all(checks)


def output_path():
    """Resolve the output directory: the grader's /output, or the local override."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_fortune(text, path):
    """Write exactly the fortune line — one line, no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    if not validate(FORTUNE):
        raise SystemExit("fortune failed validation")
    write_fortune(FORTUNE, output_path())


if __name__ == "__main__":
    main()
