from rest_framework import serializers
from novel.models import Novel


class NovelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Novel
        fields = "__all__"