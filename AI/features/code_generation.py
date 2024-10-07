
import json
from .ai_utils import send_request

def generate_code_from_prompt(prompt):
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")
    
if __name__ == "__main__":
    prompt = "Create a Python script that fetches data from an API and writes it to a file"
    result = generate_code_from_prompt(prompt)
    print("Code Generation Result:\n", result)
