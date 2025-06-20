import os


class BaseLLM:
    def __init__(self,
                 base_url: str,
                 model_name: str,
                 api_key: str = None,
                 max_tokens: int = os.getenv("MAX_TOKENS"),
                 temperature: float = os.getenv("TEMPERATURE"),
                 top_p: float = os.getenv("TOP_P"),
                 timeout: int = os.getenv("TIMEOUT"),
                 max_retries: int = os.getenv("MAX_RETRIES")
                 ) -> None:
        self.base_url = base_url
        self.model_name = model_name
        self.api_key = api_key
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.timeout = timeout
        self.max_retries = max_retries
        self.client = None

    def stream(self, prompt: str) -> iter:
        # for chunk in llm.stream(input_text):
        #     print(chunk, end="|")
        yield from self.client.stream(prompt)
