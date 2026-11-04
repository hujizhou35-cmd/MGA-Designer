"""Build the three release assets with Python 3.9+ (standard library only)."""

import hashlib
import io
import json
import re
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
NAME = "mga-designer"
SKILL = ROOT / "skills" / NAME
OUT = ROOT / "dist"


def read(path):
    """Normalize checkout line endings for reproducible builds on Windows and Unix."""
    return path.read_text(encoding="utf-8").encode("utf-8")


def archive(files):
    buffer = io.BytesIO()
    with ZipFile(buffer, "w") as output:
        for name, content in sorted(files.items()):
            entry = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            output.writestr(entry, content, compress_type=ZIP_DEFLATED, compresslevel=9)
    data = buffer.getvalue()
    with ZipFile(io.BytesIO(data)) as check:
        if check.testzip() or {n: check.read(n) for n in check.namelist()} != files:
            raise ValueError("Archive verification failed")
    return data


def portable(files):
    docs = {name: content.decode() for name, content in files.items()
            if name.startswith("references/") and name.endswith(".md")}
    anchors = {name: "guide-" + Path(name).stem for name in docs}

    def expand(name, text):
        def rewrite(match):
            label, target = match.groups()
            if target.startswith(("#", "https://", "http://", "mailto:")):
                return match.group()
            target_path = (SKILL / Path(name).parent / target).resolve()
            relative = target_path.relative_to(SKILL.resolve()).as_posix()
            if relative not in anchors:
                raise ValueError(f"Unresolved link in portable file: {name} -> {target}")
            return f"[{label}](#{anchors[relative]})"

        text = re.sub(r"\[([^\]\n]+)\]\(([^)\s]+)\)", rewrite, text)
        for path, anchor in anchors.items():
            text = text.replace(f"`{path}`", f"[{Path(path).stem}](#{anchor})")
        return text.strip()

    sections = [expand("SKILL.md", files["SKILL.md"].decode())]
    for path, text in sorted(docs.items()):
        sections.append(f'<a id="{anchors[path]}"></a>\n\n' + expand(path, text))
    sections.append("<!--\n" + files["LICENSE"].decode().strip() + "\n-->")
    return ("\n\n".join(sections) + "\n").encode()


def main():
    files = {"SKILL.md": read(SKILL / "SKILL.md"), "LICENSE": read(ROOT / "LICENSE")}
    allowed = [*SKILL.glob("agents/*.yaml"), *SKILL.glob("references/*.md")]
    for path in allowed:
        files[path.relative_to(SKILL).as_posix()] = read(path)
    unhandled = [p for p in SKILL.rglob("*") if p.is_file()
                 and p.relative_to(SKILL).as_posix() not in files]
    if unhandled:
        raise ValueError(f"Review new skill resources before shipping: {unhandled}")

    plugin = {f"skills/{NAME}/{key}": val for key, val in files.items() if key != "LICENSE"}
    plugin["LICENSE"] = files["LICENSE"]
    for path in (".codex-plugin/plugin.json", ".agents/plugins/marketplace.json"):
        plugin[path] = read(ROOT / path)
        json.loads(plugin[path])
    assets = {"SKILL.md": portable(files), f"{NAME}.skill": archive(files),
              f"{NAME}-plugin.zip": archive(plugin)}
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=OUT) as tmp:
        for name, data in assets.items():
            (Path(tmp) / name).write_bytes(data)
        for name, data in assets.items():
            (Path(tmp) / name).replace(OUT / name)
            print(hashlib.sha256(data).hexdigest(), name)


if __name__ == "__main__":
    main()
