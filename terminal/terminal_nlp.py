
import subprocess
from .ai_utils import send_request

def execute_natural_language_command(query):
    # Convert natural language command to shell command using AI
    messages = [
        {
            "role": "user",
            "content": f"Convert the following natural language command to a shell command: {query}"
        }
    ]
    response = send_request(model_key="coding", messages=messages)
    shell_command = response.get("choices", [{}])[0].get("message", {}).get("content", "")
    
    # Execute the shell command
    if shell_command:
        result = subprocess.run(shell_command, shell=True, capture_output=True, text=True)
        return result.stdout
    else:
        return "Failed to convert natural language to shell command."
    
if __name__ == "__main__":
    query = "List all JavaScript files in this directory"
    result = execute_natural_language_command(query)
    print("Terminal Command Result:\n", result)
