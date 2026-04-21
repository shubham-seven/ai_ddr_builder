# reasoning/root_cause_analyzer.py

from utils.llm_client import call_llm


def load_prompt():
    with open("prompts/root_cause_prompt.txt", "r") as f:
        return f.read()


def analyze_root_cause(data):
    prompt_template = load_prompt()

    for item in data:
        prompt = prompt_template.replace("{area}", item["area"])
        prompt = prompt.replace("{issue}", item["issue"])
        prompt = prompt.replace("{details}", item["details"])

        try:
            response = call_llm(prompt, model="pro")
            item["root_cause"] = response.strip() if response else "Not Available"

        except Exception as e:
            print(f"❌ Root cause error: {e}")
            item["root_cause"] = "Not Available"

    return data