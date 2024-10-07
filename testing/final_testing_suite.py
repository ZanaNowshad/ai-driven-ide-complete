
import json
from ..ai_utils import send_request

def run_final_tests(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Run comprehensive tests on the following code:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)"
    result = run_final_tests(code_snippet)
    print("Final Testing Result:\n", result)
