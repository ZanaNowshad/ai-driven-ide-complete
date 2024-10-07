
import json
from ..ai_utils import send_request

def code_search(query):
    messages = [
        {
            "role": "user",
            "content": f"Search the codebase for: {query}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    query = "Find all functions that handle user input"
    result = code_search(query)
    print("Code Search Result:\n", result)
