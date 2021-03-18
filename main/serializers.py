from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
