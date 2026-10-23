"""Claude Code用とCodex用のマニフェストで、同じ値を持つべき項目が一致しているかを検査する。

repositoryのルートから `python3 scripts/check_manifests.py` で実行する。
一致しない項目があれば、その項目と各ファイルの値を出力して終了コード1で終わる。
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CLAUDE_PLUGIN = ".claude-plugin/plugin.json"
CLAUDE_MARKETPLACE = ".claude-plugin/marketplace.json"
CODEX_PLUGIN = ".codex-plugin/plugin.json"
CODEX_MARKETPLACE = ".agents/plugins/marketplace.json"

# 項目ごとに、同じ値を持つべき場所を (ファイル, キーの並び) で列挙する。
# キーの並びの整数は、配列の要素の位置を表す。
CHECKS = {
    "version": [
        (CLAUDE_PLUGIN, ["version"]),
        (CODEX_PLUGIN, ["version"]),
    ],
    "name": [
        (CLAUDE_PLUGIN, ["name"]),
        (CODEX_PLUGIN, ["name"]),
        (CLAUDE_MARKETPLACE, ["plugins", 0, "name"]),
        (CODEX_MARKETPLACE, ["plugins", 0, "name"]),
    ],
    "displayName": [
        (CLAUDE_PLUGIN, ["displayName"]),
        (CODEX_PLUGIN, ["interface", "displayName"]),
    ],
    "description": [
        (CLAUDE_PLUGIN, ["description"]),
        (CODEX_PLUGIN, ["description"]),
        (CODEX_PLUGIN, ["interface", "shortDescription"]),
        (CLAUDE_MARKETPLACE, ["description"]),
        (CLAUDE_MARKETPLACE, ["plugins", 0, "description"]),
    ],
    "author": [
        (CLAUDE_PLUGIN, ["author", "name"]),
        (CODEX_PLUGIN, ["author", "name"]),
        (CODEX_PLUGIN, ["interface", "developerName"]),
        (CLAUDE_MARKETPLACE, ["owner", "name"]),
    ],
    "homepage": [
        (CLAUDE_PLUGIN, ["homepage"]),
        (CODEX_PLUGIN, ["homepage"]),
    ],
    "repository": [
        (CLAUDE_PLUGIN, ["repository"]),
        (CODEX_PLUGIN, ["repository"]),
    ],
    "keywords": [
        (CLAUDE_PLUGIN, ["keywords"]),
        (CODEX_PLUGIN, ["keywords"]),
    ],
    "skills": [
        (CLAUDE_PLUGIN, ["skills"]),
        (CODEX_PLUGIN, ["skills"]),
    ],
    "category": [
        (CODEX_PLUGIN, ["interface", "category"]),
        (CODEX_MARKETPLACE, ["plugins", 0, "category"]),
    ],
}

MISSING = "(値なし)"


def get(path, keys):
    """ファイルを読み、キーの並びをたどった先の値を返す。たどれなければMISSINGを返す。"""
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    for key in keys:
        try:
            value = value[key]
        except (KeyError, IndexError, TypeError):
            return MISSING
    return value


def main():
    failed = False
    for label, locations in CHECKS.items():
        values = {
            f"{path}: {'.'.join(map(str, keys))}": get(path, keys)
            for path, keys in locations
        }
        missing = [location for location, value in values.items() if value == MISSING]
        distinct = {json.dumps(value, ensure_ascii=False) for value in values.values()}
        if missing or len(distinct) > 1:
            failed = True
            print(f"NG: {label}")
            for location, value in values.items():
                print(f"    {location} = {json.dumps(value, ensure_ascii=False)}")

    if failed:
        return 1
    print("OK: マニフェストの共通項目はすべて一致している")
    return 0


if __name__ == "__main__":
    sys.exit(main())
