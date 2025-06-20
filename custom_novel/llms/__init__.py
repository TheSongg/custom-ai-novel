from .llm import OpenAILLMs, OllamaLLMs, XinferenceLLMs
import os


if os.getenv("INTERFACE").strip().lower() == "openai":
    llm_client = OpenAILLMs
elif os.getenv("INTERFACE").strip().lower() == "ollama":
    llm_client = OllamaLLMs
elif os.getenv("INTERFACE").strip().lower() == "xinference":
    llm_client = XinferenceLLMs
else:
    raise ValueError("Unsupported LLMs interface type!")
