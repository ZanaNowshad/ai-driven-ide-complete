
import json
from ..ai_utils import send_request

def review_code(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Review the following code and suggest improvements:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def add_numbers(a, b):\n    return a + b"
    result = review_code(code_snippet)
    print("Code Review Result:\n", result)
