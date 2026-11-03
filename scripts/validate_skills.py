"""Validate a self-contained public Agent Skills repository."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


def validate(root):
    errors = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills found in skills/*/SKILL.md")
    names = set()
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
        if not match:
            errors.append(f"{path.relative_to(root)}: missing YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(match.group(1))
        except yaml.YAMLError as error:
            errors.append(f"{path.relative_to(root)}: invalid YAML: {error}")
            continue
        if not isinstance(meta, dict):
            errors.append(f"{path.relative_to(root)}: frontmatter must be a mapping")
            continue
        name = meta.get("name", "")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{path.relative_to(root)}: invalid skill name")
            continue
        if len(name) > 64 or name != path.parent.name or name in names:
            errors.append(f"{name}: name must be unique and match its folder (max 64 characters)")
        names.add(name)
        description = meta.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append(f"{name}: description must have 1 to 1024 characters")
        if len(text.splitlines()) > 500:
            errors.append(f"{name}: move detailed references out of SKILL.md")
        if re.search(r"\[TODO(?::|\])", text, re.I):
            errors.append(f"{name}: unfinished skill instructions")
    for path in sorted(root.rglob("*.md")):
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", path.read_text(encoding="utf-8")):
            parsed = urlsplit(target.strip("<>"))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f"{path.relative_to(root)}: missing or external local target {target}")
    if not (root / "LICENSE").is_file():
        errors.append("Missing repository LICENSE")
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print(f"Validated {len(skills)} skills and local Markdown links in {root.name}")
    return not errors


if __name__ == "__main__":
    repository = Path(__file__).resolve().parents[1]
    raise SystemExit(0 if validate(repository) else 1)
