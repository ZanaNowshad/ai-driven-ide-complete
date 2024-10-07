
import json
from ai_utils import send_request

def collaborate(pair_programming_query):
    messages = [
        {
            "role": "user",
            "content": f"Assist with the following collaboration task:\n{pair_programming_query}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    query = "Write a function to merge two sorted arrays."
    result = collaborate(query)
    print("Pair Programming Review Result:\n", result)
