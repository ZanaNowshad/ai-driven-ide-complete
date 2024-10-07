
import json
from ..ai_utils import send_request

def deploy_serverless_function(code_snippet, platform="AWS Lambda"):
    messages = [
        {
            "role": "user",
            "content": f"Deploy the following code as a serverless function on {platform}:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def handler(event, context):\n    return {'statusCode': 200, 'body': 'Hello from Serverless'}"
    result = deploy_serverless_function(code_snippet)
    print("Serverless Deployment Result:\n", result)
