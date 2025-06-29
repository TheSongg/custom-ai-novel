import json

from rest_framework import status
from rest_framework.decorators import action
from django.http import StreamingHttpResponse
from custom_novel.pub.base_views import BaseViewSet


class NovelViewSet(BaseViewSet):


    def create(self, request, *args, **kwargs):
        topic = request.data.get('topic')
        category = request.data.get('category')
        user_guidance = request.data.get('user_guidance')
        #  生成核心种子
        core_seed = self.generate_novel_settings(
            "core_seed_prompt.md",
            topic=topic,
            category=category,
            user_guidance=user_guidance
        )
        #  初始化若干个角色动力学
        character_dynamics = self.generate_novel_settings(
            "character_dynamics_prompt.md",
            core_seed=core_seed,
            user_guidance=user_guidance
        )
        try:
            character_dynamics = json.loads(character_dynamics)
            #  初始化角色信息
            for character in character_dynamics:
                novel_role = self.generate_novel_settings(
                    "create_character_state_prompt.md",
                    character=character
                )
        except Exception as e:
            raise e

        #  生成世界观
        world_view = self.generate_novel_settings(
            "world_view_prompt.md",
            user_guidance=user_guidance,
            core_seed=core_seed,
        )

        #  生成三幕式情节
        plot_architecture = self.generate_novel_settings(
            "plot_architecture_prompt.md",
            user_guidance=user_guidance,
            core_seed=core_seed,
            character_dynamics=character_dynamics,
            world_view=world_view,
        )


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return StreamingHttpResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
