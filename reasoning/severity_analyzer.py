# reasoning/severity_analyzer.py

from utils.llm_client import call_llm


def load_prompt():
    with open("prompts/severity_prompt.txt", "r") as f:
        return f.read()


def analyze_severity(data):
    prompt_template = load_prompt()

    for item in data:
        prompt = prompt_template.replace("{area}", item["area"])
        prompt = prompt.replace("{issue}", item["issue"])
        prompt = prompt.replace("{details}", item["details"])

        try:
            response = call_llm(prompt, model="pro")

            # Basic parsing
            item["severity"] = response.strip() if response else "Not Available"

        except Exception as e:
            print(f"❌ Severity error: {e}")
            item["severity"] = "Not Available"

    return data