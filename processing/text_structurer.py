# processing/text_structurer.py

import json
from utils.llm_client import call_llm


def load_prompt():
    with open("prompts/extraction_prompt.txt", "r") as f:
        return f.read()


def safe_parse_json(response):
    try:
        return json.loads(response)
    except Exception as e:
        print(f"⚠️ JSON Parse Failed: {e}")
        return []


def chunk_text(text, max_chars=2000):
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]


def structure_text(text_data, source="inspection", max_chunks=2):
    prompt_template = load_prompt()
    structured_results = []

    for page in text_data:
        raw_text = page["text"]

        if not raw_text.strip():
            continue

        chunks = chunk_text(raw_text)

        # ✅ LIMIT chunks (IMPORTANT)
        chunks = chunks[:max_chunks]

        for chunk in chunks:
            prompt = prompt_template.replace("{input_text}", chunk)

            try:
                response = call_llm(prompt, model="flash")
                parsed = safe_parse_json(response)

                # Attach metadata
                for item in parsed:
                    item["page"] = page["page"]
                    item["source"] = source

                structured_results.extend(parsed)

            except Exception as e:
                print(f"❌ Error on page {page['page']}: {e}")

    return structured_results