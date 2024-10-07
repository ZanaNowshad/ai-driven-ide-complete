
import json
from .ai_utils import send_request

def get_autocompletion(prompt):
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")
    
if __name__ == "__main__":
    prompt = "Write a function to reverse a string in Python"
    result = get_autocompletion(prompt)
    print("Autocompletion Result:\n", result)
