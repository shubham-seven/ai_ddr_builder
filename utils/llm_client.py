# utils/llm_client.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model mapping
MODEL_MAP = {
    "flash": "gemini-2.5-flash",
    "pro": "gemini-2.5-pro"
}


def call_llm(prompt: str, model: str = "flash"):
    try:
        model_name = MODEL_MAP.get(model, "gemini-1.5-flash")

        llm = genai.GenerativeModel(model_name)

        response = llm.generate_content(prompt)

        if response.text:
            return response.text.strip()
        else:
            return ""

    except Exception as e:
        print(f"❌ LLM Error ({model}): {e}")
        return ""