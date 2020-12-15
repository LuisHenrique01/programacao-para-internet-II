from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from core.models import Profile, Post, Comment

class ProfileSerializer(ModelSerializer):
    
    class Meta:
        model = Profile
        exclude = ['id']