#!/usr/bin/env python3
"""Przygotowuje katalog dokumentacji do builda Zensical.

Kopiuje `docs/` -> `build/docs/` i konwertuje alerty w stylu GitHub
(`> [!NOTE]`) na admonitiony Zensical/MkDocs (`!!! note`).

Dzięki temu pliki źródłowe w `docs/` pozostają czystym GFM-em (ładnie
renderowanym bezpośrednio na GitHubie), a strona Zensical dostaje
składnię, którą natywnie potrafi ostylować jako kolorowe bloki.

Użycie:
    python scripts/prepare_docs.py        # przed `zensical build` / `serve`
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs"
DST = ROOT / "build" / "docs"

# Mapowanie typów alertów GitHub -> typy admonition Zensical/Material.
ALERT_MAP = {
    "NOTE": "note",
    "TIP": "tip",
    "IMPORTANT": "info",
    "WARNING": "warning",
    "CAUTION": "danger",
}

# Obsługuje też alerty wcięte (np. wewnątrz listy) — grupa `indent`.
ALERT_RE = re.compile(
    r"^(?P<indent>[ \t]*)>\s*\[!(?P<type>NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$"
)


def _dequote(line: str) -> str:
    """Usuwa prefiks cytatu blokowego, zachowując wewnętrzne wcięcia."""
    if line.startswith("> "):
        return line[2:]
    if line == ">":
        return ""
    return line[1:]  # ">tekst" -> "tekst"


def convert(text: str) -> tuple[str, int]:
    """Zamienia bloki alertów GitHub na admonitiony. Zwraca (tekst, liczba_bloków)."""
    lines = text.splitlines()
    out: list[str] = []
    converted = 0
    i = 0
    while i < len(lines):
        match = ALERT_RE.match(lines[i])
        if not match:
            out.append(lines[i])
            i += 1
            continue
        indent = match.group("indent")
        # Zbierz ciało cytatu — kolejne linie z tym samym wcięciem i prefiksem ">".
        i += 1
        body: list[str] = []
        while i < len(lines) and lines[i].startswith(f"{indent}>"):
            body.append(_dequote(lines[i][len(indent):]))
            i += 1
        out.append(f"{indent}!!! {ALERT_MAP[match.group('type')]}")
        out.append("")
        out.extend(f"{indent}    {b}" if b.strip() else "" for b in body)
        converted += 1
    result = "\n".join(out)
    if text.endswith("\n"):
        result += "\n"
    return result, converted


def main() -> int:
    if not SRC.is_dir():
        print(f"BŁĄD: nie znaleziono katalogu {SRC}", file=sys.stderr)
        return 1

    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)

    total_files = 0
    total_blocks = 0
    for md in sorted(DST.rglob("*.md")):
        new_text, count = convert(md.read_text(encoding="utf-8"))
        if count:
            md.write_text(new_text, encoding="utf-8")
            total_files += 1
            total_blocks += count
            print(f"  {md.relative_to(ROOT)}: {count} admonition(s)")

    print(
        f"Gotowe: skonwertowano {total_blocks} bloków w {total_files} plikach "
        f"-> {DST.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
