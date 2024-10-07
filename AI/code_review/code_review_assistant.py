
import json
from ..ai_utils import send_request

def code_review_assistant(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Review the following code for improvements and potential issues:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def add_numbers(a, b):\n    return a + b"
    result = code_review_assistant(code_snippet)
    print("Code Review Result:\n", result)
