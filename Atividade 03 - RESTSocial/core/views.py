from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, status
from rest_framework.views import APIView
from core.models import Profile, Post, Comment
from core.serializers import ProfileSerializer, ProfilePostSerializer, PostSerializer, CommentSerializer, TotaPostsCommentsSerializer
# Create your views here.

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    
class ProfilePostView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    
    
class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    
    def get_queryset(self):
        queryset = Comment.objects.filter(postId=self.kwargs.get('postId'))
        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data
        simple_data = {
            'name': data['name'],
            'email': data['email'],
            'body': data['body'],
            'postId': kwargs.get('postId')
        } 
        serializer = self.get_serializer(data=simple_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = Comment.objects.filter(postId=self.kwargs.get('postId'))
        return queryset
    
    
class TotaPostsCommentsView(APIView):
    
    def get(self, request, *args, **kargs):
        user = Profile.objects.get(id=kargs['pk'])
        total_posts = user.total_posts()
        total_comments = user.total_comments()
        data = {'pk': user.id, 
                'name': user.name,
                'total_posts': total_posts,
                'total_comments': total_comments}
        serializer = TotaPostsCommentsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ApiRootView(APIView):
    
    def get(self, request, *args, **kargs):
        return Response({'profile': reverse('Profile', request=request),
                         'profile-posts': reverse('ProfilePost', request=request),
                         'post': reverse('Post', request=request),
                         })