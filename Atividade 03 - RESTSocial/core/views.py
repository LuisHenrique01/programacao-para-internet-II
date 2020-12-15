from django.shortcuts import render
from rest_framework import generics
from core.models import Profile, Post, Comment
from core.serializers import ProfileSerializer
# Create your views here.

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer