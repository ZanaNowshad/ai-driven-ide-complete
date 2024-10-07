
import json
from ..ai_utils import send_request

def suggest_api_integration(functionality_description):
    messages = [
        {
            "role": "user",
            "content": f"Suggest an API to integrate for the following functionality:\n{functionality_description}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    functionality_description = "Implement a payment gateway for an e-commerce platform."
    result = suggest_api_integration(functionality_description)
    print("API Integration Suggestion:\n", result)
