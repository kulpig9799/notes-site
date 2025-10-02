"""
Convert all .txt in a folder to Markdown under docs/notes/ (creating it if needed).
Usage:
    python scripts/convert_txt_to_md.py /path/to/txt_folder
"""
import os, sys, re, unicodedata, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS_NOTES = ROOT / "docs" / "notes"
DOCS_NOTES.mkdir(parents=True, exist_ok=True)

def slugify(value: str) -> str:
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^a-zA-Z0-9\-_ \s]', '', value)
    value = re.sub(r'\s+', '-', value).strip('-')
    return value.lower() or "ghi-chu"

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/convert_txt_to_md.py /path/to/txt_folder")
        sys.exit(1)
    src = pathlib.Path(sys.argv[1])
    if not src.exists():
        print(f"Folder not found: {src}")
        sys.exit(1)

    added = []
    for p in src.rglob("*.txt"):
        title = p.stem
        slug = slugify(title)
        dest = DOCS_NOTES / f"{slug}.md"
        content = p.read_text(encoding="utf-8", errors="ignore")
        dest.write_text(f"# {title}\n\n{content}\n", encoding="utf-8")
        added.append((title, f"notes/{dest.name}"))
        print(f"Converted: {p.name} -> {dest.relative_to(ROOT)}")

    if added:
        print("\n--- Paste the following into mkdocs.yml under 'nav' ---")
        print("  - Ghi chú:")
        for title, rel in added:
            print(f"      - \"{title}\": {rel}")
    else:
        print("No .txt files found.")

if __name__ == "__main__":
    main()