"""Emit the bundled news collage as the contest entry image."""

import pathlib


def main() -> None:
    folder = pathlib.Path(__file__).resolve().parent
    artwork = folder / "entry.png"
    picture_bytes = artwork.read_bytes()
    if not picture_bytes:
        raise ValueError("bundled collage is empty")
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    result = out_dir / "entry.png"
    result.write_bytes(picture_bytes)


if __name__ == "__main__":
    main()
