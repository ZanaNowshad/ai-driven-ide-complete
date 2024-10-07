
import json
from ..ai_utils import send_request

def compliance_check(code_snippet, compliance_standard="GDPR"):
    messages = [
        {
            "role": "user",
            "content": f"Check the following code for compliance with {compliance_standard}:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "def collect_user_data():\n    user_data = {'name': 'John', 'email': 'john@example.com'}\n    return user_data"
    result = compliance_check(code_snippet)
    print("Compliance Check Result:\n", result)
