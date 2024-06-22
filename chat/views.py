from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message

@login_required
def chatroom_list(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chat/chatroom_list.html', {'chatrooms': chatrooms})

@login_required
def chatroom_detail(request, room_id):
    chatroom = ChatRoom.objects.get(id=room_id)
    messages = Message.last_10_messages(chatroom)
    return render(request, 'chat/chatroom_detail.html', {
        'chatroom': chatroom,
        'messages': messages,
        'username': request.user.username
    })


