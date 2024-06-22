from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatroom_list, name='chatroom_list'),
    path('rooms/<int:room_id>/', views.chatroom_detail, name='chatroom_detail'),
]
