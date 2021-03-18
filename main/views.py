from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import PostSerializer, PostListSerializer
from .models import Post
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response


class Index(generics.CreateAPIView):
    serializer_class = PostSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwner,)


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
