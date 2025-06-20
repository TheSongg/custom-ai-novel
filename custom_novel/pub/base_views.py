from rest_framework import viewsets
import os
from novel.models import Novel
from novel.serializers import NovelSerializer
from pub.prompt import prompt_template
from llms import llm_client


class BaseViewSet(viewsets.ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer

    def __init__(self):
        super(BaseViewSet, self).__init__()
        self.client = llm_client(
            base_url=os.getenv("BASE_URL"),
            model_name=os.getenv("model_name"),
            api_key=os.getenv("API_KEY"),
            max_tokens= int(os.getenv("MAX_TOKENS")),
            temperature= int(os.getenv("TEMPERATURE")),
            top_p=int(os.getenv("TOP_P")),
            timeout=int(os.getenv("TIMEOUT")),
            max_retries=int(os.getenv("MAX_RETRIES"))
        )


    def generate_novel_settings(self, prompt_template_name, **kwargs):
        prompt = prompt_template.get_prompt(prompt_template_name, **kwargs)
        return self.client.stream(prompt)
