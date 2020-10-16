from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post
from users.models import Profile
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer, ProfileSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer