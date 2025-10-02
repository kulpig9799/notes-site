"""
Convert all .docx in a folder to Markdown under a target docs subfolder.
Usage:
    python scripts/convert_docx_to_md.py /path/to/docx_folder docs/<muc>
Requires:
    - Either Pandoc installed (preferred), or
    - python-docx: pip install python-docx
"""
import os, sys, subprocess, shutil, pathlib

def use_pandoc(src_file: pathlib.Path, dest_file: pathlib.Path) -> bool:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return False
    try:
        subprocess.check_call([pandoc, str(src_file), "-f", "docx", "-t", "markdown", "-o", str(dest_file)])
        return True
    except subprocess.CalledProcessError:
        return False

def use_python_docx(src_file: pathlib.Path, dest_file: pathlib.Path) -> bool:
    try:
        import docx
    except ImportError:
        return False
    doc = docx.Document(str(src_file))
    lines = []
    for p in doc.paragraphs:
        lines.append(p.text)
    dest_file.write_text("# " + src_file.stem + "\n\n" + "\n\n".join(lines) + "\n", encoding="utf-8")
    return True

def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/convert_docx_to_md.py /path/to/docx_folder docs/<muc>")
        sys.exit(1)
    src = pathlib.Path(sys.argv[1])
    target = pathlib.Path(sys.argv[2])
    if not src.exists():
        print(f"Folder not found: {src}")
        sys.exit(1)
    target.mkdir(parents=True, exist_ok=True)

    for p in src.rglob("*.docx"):
        dest = target / (p.stem + ".md")
        if use_pandoc(p, dest):
            print(f"[pandoc] {p.name} -> {dest}")
        elif use_python_docx(p, dest):
            print(f"[python-docx] {p.name} -> {dest}")
        else:
            print(f"Cannot convert {p.name}. Please install pandoc OR `pip install python-docx`.")

if __name__ == "__main__":
    main()