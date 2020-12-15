from django.urls import path
from core.views import ProfileView

urlpatterns = [
    path('profiles/', ProfileView.as_view())
]
