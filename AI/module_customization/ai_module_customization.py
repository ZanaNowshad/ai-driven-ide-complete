
import json
from ..ai_utils import send_request

def customize_ai_module(module_description, customization_options):
    messages = [
        {
            "role": "user",
            "content": f"Customize the AI module for the following purpose:\n{module_description}\nOptions: {customization_options}"
        }
    ]
    response = send_request(model_key="general", messages=messages)
    return response.get("choices", [{}])[0].get("message", {}).get("content", "")

if __name__ == "__main__":
    module_description = "Create a personalized AI assistant for code refactoring."
    customization_options = "Should prioritize performance improvements and adhere to PEP8 standards."
    result = customize_ai_module(module_description, customization_options)
    print("Customized AI Module:\n", result)
