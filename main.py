"""Emit the news-image-01 v3 front page.

The competition entry is a single pre-rendered picture that sums up the
world's news of Friday 13 November 2026. This runner does nothing clever:
it locates the bundled entry.png next to this script, reads its bytes, and
drops an identical copy at /output/entry.png so the grader can pick it up.
No network, no randomness, no image processing — the file is reproduced
exactly as it was submitted.
"""

from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source_path = here / "entry.png"
    image_bytes = source_path.read_bytes()
    target_dir = Path("/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.png"
    destination.write_bytes(image_bytes)
    written_back = destination.read_bytes()
    assert len(written_back) == len(image_bytes), "output size mismatch"
    print(f"Wrote {destination} ({len(image_bytes)} bytes)")


if __name__ == "__main__":
    main()
