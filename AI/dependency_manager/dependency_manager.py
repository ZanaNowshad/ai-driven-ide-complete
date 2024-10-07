
import json
from ..ai_utils import send_request

def check_and_update_dependencies():
    messages = [
        {
            "role": "user",
            "content": "Analyze the project's dependencies and suggest any updates or identify vulnerabilities."
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    result = check_and_update_dependencies()
    print("Dependency Check Result:\n", result)
