
import json
from ..ai_utils import send_request

def setup_ci_cd_pipeline(project_name):
    messages = [
        {
            "role": "user",
            "content": f"Set up a CI/CD pipeline for the project: {project_name}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    project_name = "AI-Driven IDE"
    result = setup_ci_cd_pipeline(project_name)
    print("CI/CD Setup Result:\n", result)
