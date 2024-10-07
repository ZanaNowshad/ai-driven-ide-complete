
import json
from ..ai_utils import send_request

def task_planner(feature_description):
    messages = [
        {
            "role": "user",
            "content": f"Break down the following feature into actionable tasks and provide time estimates:\n{feature_description}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    feature_description = "Implement a user authentication system with email verification and password reset functionality."
    result = task_planner(feature_description)
    print("Task Planner Result:\n", result)
