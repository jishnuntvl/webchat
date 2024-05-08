import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message
from asgiref.sync import sync_to_async # type: ignore
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_layer 
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        frienduname = text_data_json["frienduname"]
        message_instance=await self.save_message(message, username, frienduname)
        message_time = message_instance.date.strftime("%H:%M")
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message_instance.value , 
                "username" : message_instance.sender.username ,
                "frienduname":message_instance.receiver.username,
                "time":message_time
            })
    async def sendMessage(self , event) : 
        message = event["message"]
        username = event["username"]
        frienduname=event["frienduname"]
        time=event["time"]
        await self.send(text_data = json.dumps({"message":message ,"username":username,"frienduname":frienduname,"time":time}))  

    @sync_to_async
    def save_message(self,message, username, frienduname):
        sender=User.objects.get(username=username)
        receiver=User.objects.get(username=frienduname)
        return (Message.objects.create(value=message,sender=sender,receiver=receiver))     