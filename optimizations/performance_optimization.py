
import json
from ..ai_utils import send_request

def optimize_code_performance(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Optimize the performance of the following code:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def calculate_sum(arr):\n    return sum(arr)"
    result = optimize_code_performance(code_snippet)
    print("Performance Optimization Result:\n", result)
