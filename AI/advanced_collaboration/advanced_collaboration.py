
import json
from ..ai_utils import send_request

def conflict_resolution_assistant(branch_a, branch_b):
    messages = [
        {
            "role": "user",
            "content": f"Resolve conflicts between the following branches:\nBranch A: {branch_a}\nBranch B: {branch_b}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    branch_a = "feature/auth"
    branch_b = "feature/ui-improvements"
    result = conflict_resolution_assistant(branch_a, branch_b)
    print("Conflict Resolution Result:\n", result)
