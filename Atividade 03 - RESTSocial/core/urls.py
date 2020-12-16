from django.urls import path
from core.views import ProfileView, ProfileDetailView, ProfilePostView, PostView, PostDetailView, CommentView, CommentDetailView

urlpatterns = [
    path('profiles/', ProfileView.as_view(), name='Profile'),
    path('profiles/<int:pk>', ProfileDetailView.as_view(), name='ProfileDetail'),
    path('profile-posts/', ProfilePostView.as_view(), name='ProfilePost'),
    path('posts-comments/', PostView.as_view(), name='Post'),
    path('posts-comments/<int:pk>/', PostDetailView.as_view(), name='PostDetail'),
    path('posts/<int:postId>/comments/', CommentView.as_view(), name='PostsComments'),
    path('posts/<int:postId>/comments/<int:pk>/', CommentDetailView.as_view(), name='PostsCommentsDetail'),
]
