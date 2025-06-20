from rest_framework import status
from rest_framework.decorators import action
from django.http import StreamingHttpResponse
from pub.base_views import BaseViewSet


class NovelViewSet(BaseViewSet):


    def create(self, request, *args, **kwargs):
        topic = request.data.get('topic')
        category = request.data.get('category')
        user_guidance = request.data.get('user_guidance')
        core_seed = self.generate_novel_settings("core_seed_prompt.md",
                                                 topic=topic,
                                                 category=category,
                                                 user_guidance=user_guidance
                                                 )
        character_dynamics = self.generate_novel_settings("character_dynamics_prompt.md",
                                                          core_seed=core_seed,
                                                          user_guidance=user_guidance
                                                          )


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return StreamingHttpResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
