"""Write the one-word entry username to /output/entry.txt, no trailing newline."""

from pathlib import Path

entry_path = Path("/output/entry.txt")
entry_path.parent.mkdir(parents=True, exist_ok=True)
entry_path.write_text("calm-lynx-73", encoding="utf-8")
