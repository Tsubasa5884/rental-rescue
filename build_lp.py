"""products.json と .env の設定から、LP 用の products.js を作る。

使い方:  python web_lp/build_lp.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config  # noqa: E402


def build_lp():
    products = []
    if config.PRODUCTS_JSON.exists():
        products = json.loads(config.PRODUCTS_JSON.read_text(encoding="utf-8"))
    site = {
        "ownerName": config.SITE_OWNER_NAME,
        "primeUrl": config.PRIME_TRIAL_URL,
        "audibleUrl": config.AUDIBLE_TRIAL_URL,
        "categories": {k: v["label"] for k, v in config.CATEGORIES.items()},
    }
    js = (
        "// このファイルは build_lp.py が自動で作ります。直接書き換えないでください。\n"
        f"window.SITE = {json.dumps(site, ensure_ascii=False, indent=2)};\n"
        f"window.PRODUCTS = {json.dumps(products, ensure_ascii=False, indent=2)};\n"
    )
    out = config.LP_DIR / "products.js"
    out.write_text(js, encoding="utf-8")
    print(f"LP のデータを {out.name} に書き出しました（{len(products)} 件）")


if __name__ == "__main__":
    build_lp()
