from django.urls import path
from api import views as v 

urlpatterns = [
    path('list/', v.game_list, name='game_list'),
    path('detail/<int:pk>/', v.game_detail)
]