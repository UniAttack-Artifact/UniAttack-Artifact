import json
import re

def txt_to_json(input_txt_path: str, output_json_path: str):
    with open(input_txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 按 Prompt 块切分
    blocks = re.split(r"-{3}\s*Prompt\s+\d+\s*-{3}", text)

    results = []

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # 1. 提取 Z = xxx 作为 prompt
        z_match = re.search(r"Z\s*=\s*(.+)", block)
        if not z_match:
            continue
        prompt = z_match.group(1).strip()

        # 2. 提取 Response 内容
        response_match = re.search(
            r"-{3}\s*Response\s+\d+\s*-{3}(.*?)(={5,}|$)",
            block,
            re.DOTALL
        )
        if not response_match:
            continue

        response = response_match.group(1).strip()

        results.append({
            "prompt": prompt,
            "response": response
        })

    # 3. 保存为 JSON
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"[OK] 转换完成，共生成 {len(results)} 条样本")
    print(f"[OK] 输出文件：{output_json_path}")


if __name__ == "__main__":
    txt_to_json(
        input_txt_path="deepseek_responses_pairs20251229_134014.txt",
        output_json_path="deepseek_responses_pairs20251229_134014.json"
    )
