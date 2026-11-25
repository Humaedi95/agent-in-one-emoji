#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes a single emoji to /output/entry.txt: the octopus, 🐙 (U+1F419).

Why the octopus, against the judge's criteria:
- At a glance: one familiar animal silhouette — a round head with eight
  arms — reads instantly even at small size, no detail needed.
- Specific to how the agent works: an agent juggles many tools, tasks and
  conversations in parallel, like eight arms working at once, and it is
  clever and adaptable — exactly what an octopus is known for.
- Distinctive: far from the obvious robot or smiley that half the field
  will send; a living, thinking creature with many arms doing many things.
"""

import os

EMOJI = "\U0001F419"  # 🐙 OCTOPUS


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read back and confirm the gate: exactly one character, not whitespace.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != EMOJI:
        raise SystemExit(f"entry.txt must hold exactly the octopus, got {written!r}")


if __name__ == "__main__":
    main()
