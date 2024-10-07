
import json
from ..ai_utils import send_request

def security_scan(code_snippet):
    messages = [
        {
            "role": "user",
            "content": f"Perform a security scan on the following code and identify vulnerabilities:\n{code_snippet}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    code_snippet = "import os\ndef delete_file(file_path):\n    os.remove(file_path)"
    result = security_scan(code_snippet)
    print("Security Scan Result:\n", result)
