
import json
from .ai_utils import send_request

def ai_chat(query):
    messages = [
        {
            "role": "user",
            "content": query
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")
    
if __name__ == "__main__":
    query = "How do I set up an Express.js server?"
    result = ai_chat(query)
    print("AI Chat Result:\n", result)
