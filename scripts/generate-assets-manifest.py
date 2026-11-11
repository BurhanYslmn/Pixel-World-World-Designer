#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets-manifest.js"
EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"}

CATEGORIES = {
    "blocks": "Blocks",
    "backgrounds": "Backgrounds",
    "props": "Props",
    "worlds": "Orbs",
}

EXCLUDED = {
    "backgrounds": {"recipes-preview.webp", "recipes-map-preview.webp"},
}


def image_files(folder: str, excluded: set[str]) -> list[str]:
    directory = ROOT / folder
    if not directory.exists():
        return []

    return sorted(
        (
            path.name
            for path in directory.iterdir()
            if path.is_file()
            and path.suffix.lower() in EXTENSIONS
            and path.name not in excluded
        ),
        key=str.casefold,
    )


def main() -> None:
    manifest = {
        "version": 1,
        **{
            category: image_files(folder, EXCLUDED.get(category, set()))
            for category, folder in CATEGORIES.items()
        },
    }

    content = "window.PIXEL_WORLDS_ASSETS = " + json.dumps(
        manifest,
        ensure_ascii=False,
        separators=(",", ":"),
    ) + ";\n"

    OUTPUT.write_text(content, encoding="utf-8")

    total = sum(len(manifest[key]) for key in CATEGORIES)
    print(f"Generated {OUTPUT.name}: {total} assets")
    for category in CATEGORIES:
        print(f"  {category}: {len(manifest[category])}")


if __name__ == "__main__":
    main()
