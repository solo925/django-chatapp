from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.chatroom_list, name='chatroom_list'),
    path('rooms/<int:room_id>/', views.chatroom_detail, name='chatroom_detail'),
    path('', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.Logout, name='logout'),
    path('createroom/', views.create_chatroom, name='room'),
]
