
# AI Configuration for the IDE

API_BASE = "https://api.deepinfra.com/v1/openai/chat/completions"

MODELS = {
    "coding": {
        "name": "Qwen/Qwen2.5-72B-Instruct",
        "max_input_tokens": 32000,
        "supports_function_calling": True
    },
    "general": {
        "name": "meta-llama/Meta-Llama-3.1-70B-Instruct",
        "max_input_tokens": 128000,
        "supports_function_calling": True
    },
    "embedding": {
        "name": "BAAI/bge-m3",
        "type": "embedding",
        "max_tokens_per_chunk": 8192,
        "max_batch_size": 50
    }
}
