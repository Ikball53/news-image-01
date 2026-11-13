"""news-image-01 v2 entry runner.

The bundled front-page artwork (entry.png) ships next to this script.
Running this module places an exact copy of that artwork at
/output/entry.png. Because the operation is a plain byte copy, every run
yields the identical file.
"""

import hashlib
import os
import shutil
from pathlib import Path


# The artwork is a single self-contained file; no network is used anywhere.


def _find_artwork() -> Path:
    """Locate the bundled entry.png beside this file (or in the cwd)."""
    sibling = Path(__file__).resolve().parent / "entry.png"
    if sibling.is_file():
        return sibling
    return Path.cwd() / "entry.png"


def _place_copy(artwork: Path, out_dir: Path) -> Path:
    """Copy artwork into out_dir and return the destination path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(artwork, dest)
    return dest


def main() -> None:
    src = _find_artwork()
    target = Path(os.environ.get("OUTPUT_DIR", "/output"))
    written = _place_copy(src, target)
    checksum = hashlib.sha256(written.read_bytes()).hexdigest()
    print(f"wrote {written} sha256={checksum}")


if __name__ == "__main__":
    main()
