from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from core.models import Profile, Post, Comment

class ProfileSerializer(ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'
        
    
class ProfilePostSerializer(ModelSerializer):
    posts = StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Profile
        fields = ['name', 'email', 'address', 'posts']
        
        
class PostSerializer(ModelSerializer):
    comments = SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = Post
        fields = ['title', 'body', 'userId', 'comments']
        
        
class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'