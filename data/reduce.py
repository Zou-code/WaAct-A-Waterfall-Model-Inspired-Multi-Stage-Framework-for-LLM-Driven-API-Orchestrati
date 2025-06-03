

import os
import json
# import yaml
from dataclasses import asdict
from pprint import pprint

# ====== 引入你自己的 reduce_openapi_spec 函数和相关类 ======
from util.oas_util import reduce_openapi_spec  # 请替换为你代码文件名（无 .py 后缀）

# ====== 你原始的 OpenAPI 文件路径 ======
OPENAPI_FILE = "restbench/apis/original_spotify_oas.json"  # or "openapi.json"

# ====== 读取 OpenAPI 文件 ======
def load_openapi_spec(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# ====== 主流程 ======
def main():
    print(f"📂 Loading OpenAPI file: {OPENAPI_FILE}")
    spec = load_openapi_spec(OPENAPI_FILE)

    # if isinstance(spec, list):
    #     print("⚠️  Loaded spec is a list. Using the first item.")
    #     spec = spec[0]

    print("🔧 Reducing OpenAPI spec...")
    reduced_spec = reduce_openapi_spec(
        spec,
        dereference=True,
        only_required=True,
        merge_allof=True
    )

    print("✅ Reduction complete. Sample output:")
    pprint(reduced_spec)

    print("\n💾 Saving reduced spec to reduced_spec.json")
    with open("reduced_spec.json", "w", encoding="utf-8") as f:
        json.dump(asdict(reduced_spec), f, indent=2, ensure_ascii=False)

    print("🎉 Done!")

if __name__ == "__main__":
    main()