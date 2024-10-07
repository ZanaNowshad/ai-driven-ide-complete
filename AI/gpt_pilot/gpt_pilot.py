
import json
from ..ai_utils import send_request

def generate_project_from_idea(idea):
    messages = [
        {
            "role": "user",
            "content": f"Create a full-stack web application: {idea}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")
    
if __name__ == "__main__":
    idea = "Create a task management app with React frontend, Node.js backend, and MongoDB database."
    result = generate_project_from_idea(idea)
    print("Project Generation Result:\n", result)
