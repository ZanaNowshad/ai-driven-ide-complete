
import json
from ..ai_utils import send_request

def pair_programming_review(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Review the following code for improvements:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def multiply_numbers(a, b):\n    return a * b"
    result = pair_programming_review(code_snippet)
    print("Pair Programming Review Result:\n", result)
