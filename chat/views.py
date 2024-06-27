from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import ChatRoom, Message
from . forms import *
from django.contrib import messages


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

@login_required
def create_chatroom(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            chatroom = form.save()
            messages.success(request, f"Chatroom '{chatroom.name}' created successfully!")
            return redirect('chatroom_list')
    else:
        form = RoomForm()

    context = {'form': form}
    return render(request, 'chat/create.html', context)



def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Account created {username}")
            return redirect('login')
    else:
            form=RegisterForm()
    return render(request,"chat/register.html",{"form":form})
    
def Login(request):
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('chatroom_list')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    else:
        form=LoginForm()
    return render(request,"chat/login.html",{"form":form})


def Logout(request):
    logout(request)
    
    return render(request,"login")


