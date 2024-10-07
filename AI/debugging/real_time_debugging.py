
import json
from ..ai_utils import send_request

def real_time_debug(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Debug the following code snippet and identify issues:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def add_numbers(a, b):\nreturn a + b\nprint(add_numbers(5)"
    result = real_time_debug(code_snippet)
    print("Debugging Result:\n", result)
