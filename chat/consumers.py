import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom, Message
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        username = data.get('username')
        room = data.get('room')
        file = data.get('file')

        user = await self.get_user(username)
        chatroom = await self.get_chatroom(room)

        if user and chatroom:
            if message:
                await self.save_message(user, chatroom, message)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message,
                        'username': username
                    }
                )
            if file:
                await self.save_file(user, chatroom, file)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_file',
                        'file': file,
                        'username': username
                    }
                )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def chat_file(self, event):
        file = event['file']
        username = event['username']

        await self.send(text_data=json.dumps({
            'file': file,
            'username': username
        }))

    @sync_to_async
    def get_user(self, username):
        return User.objects.get(username=username)

    @sync_to_async
    def get_chatroom(self, room_name):
        return ChatRoom.objects.get(name=room_name)

    @sync_to_async
    def save_message(self, user, chatroom, message):
        return Message.objects.create(user=user, chatroom=chatroom, content=message)

    @sync_to_async
    def save_file(self, user, chatroom, file):
        return Message.objects.create(user=user, chatroom=chatroom, file=file)
