import json

input_path = "deepseek-r_prompt_response.jsonl"
output_path = "deepseek-r_prompt_response.json"

results = []

with open(input_path, "r", encoding="utf-8") as f:
    for line_id, line in enumerate(f):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            results.append({
                "prompt": obj["prompt"],
                "response": obj["response"]
            })
        except Exception as e:
            print(f"[Skip line {line_id}] {e}")

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
