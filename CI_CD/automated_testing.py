
import json
from ..ai_utils import send_request

def generate_test_cases(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Generate test cases for the following code:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def divide_numbers(a, b):\n    if b != 0:\n        return a / b\n    else:\n        return 'Division by zero error'"
    result = generate_test_cases(code_snippet)
    print("Generated Test Cases:\n", result)
