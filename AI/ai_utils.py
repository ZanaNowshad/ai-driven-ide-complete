
import requests
import json
from .ai_config import API_BASE, MODELS

def send_request(model_key, messages, stream=False):
    model_info = MODELS.get(model_key)
    if not model_info:
        raise ValueError(f"Model key '{model_key}' not found in AI configuration.")

    data = {
        "model": model_info["name"],
        "messages": messages
    }
    
    if stream:
        data["stream"] = True

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(API_BASE, headers=headers, json=data)
    return response.json() if not stream else response.iter_lines()
