import os

from langchain_openai import OpenAI
from langchain_xinference import Xinference
from langchain_community.llms.ollama import Ollama
from .base import BaseLLM


class OpenAILLMs(BaseLLM):
    def __init__(self,
                 base_url: str,
                 model_name: str,
                 api_key: str = None,
                 max_tokens: int = os.getenv("MAX_TOKENS"),
                 temperature: float = os.getenv("TEMPERATURE"),
                 top_p: float = os.getenv("TOP_P"),
                 timeout: int = os.getenv("TIMEOUT"),
                 max_retries: int = os.getenv("MAX_RETRIES"),
                 ):
        super().__init__(base_url, model_name, api_key, max_tokens, temperature, top_p, timeout, max_retries)

        self.client = OpenAI(
            model=self.model_name,
            api_key=self.api_key,
            base_url=self.base_url,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            timeout=self.timeout,
            max_retries=self.max_retries,
        )


class OllamaLLMs(BaseLLM):
    def __init__(self,
                 base_url: str,
                 model_name: str,
                 api_key: str = None,
                 max_tokens: int = os.getenv("MAX_TOKENS"),
                 temperature: float = os.getenv("TEMPERATURE"),
                 top_p: float = os.getenv("TOP_P"),
                 timeout: int = os.getenv("TIMEOUT")
                 ):
        super().__init__(base_url, model_name, api_key, max_tokens, temperature, top_p, timeout)

        self.client = Ollama(
            model=self.model_name,
            auth=self.api_key,
            base_url=self.base_url,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            timeout=self.timeout
        )


class XinferenceLLMs(BaseLLM):
    def __init__(self,
                 base_url: str,
                 model_name: str,
                 api_key: str = None,
                 max_tokens: int = os.getenv("MAX_TOKENS"),
                 temperature: float = os.getenv("TEMPERATURE"),
                 top_p: float = os.getenv("TOP_P"),
                 timeout: int = os.getenv("TIMEOUT")
                 ):
        super().__init__(base_url, model_name, api_key, max_tokens, temperature, top_p, timeout)

        self.client = Xinference(
            model_uid=self.model_name,
            api_key=self.api_key,
            server_url=self.base_url,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            timeout=self.timeout
        )


__all__ = ['OpenAILLMs', 'OllamaLLMs', 'XinferenceLLMs']