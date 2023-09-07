from django.contrib.auth import get_user_model
import json
from .models import *
from core.models import *
user = get_user_model()
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.utils import formats
from django.contrib.auth.models import User
import threading
from allauth.account.decorators import verified_email_required


class ChatConsumer(WebsocketConsumer):
    @verified_email_required
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat__%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()  
        
    #################SEND MESSAGE IN GROUP CHAT
    @verified_email_required
    def send_message(self,message):
        self.send(text_data=json.dumps(message))
        
    @verified_email_required    
    def fetch_messages(self, data):
        messages = []
        content = {
           'command': 'messages',
           'messages': self.messages_to_json(messages)
        }
        self.send_message(content)
        
    ###################FETCH OLD MESSAGE AND CONVERT TO JSON
    @verified_email_required
    def messages_to_json(self,messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    @verified_email_required
    def new_message(self, data):
        message = []
        content = {
            'command':'new_message',
            'message':self.message_to_json(message)
        }  

        return self.send_chat_message(content)
    

    @verified_email_required
    def message_to_json(self,message):
        return { } 
    
    @verified_email_required
    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type': 'chat_message',
                'message': message 
            }
        )
        
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
        
    
    ##########################RECEIVE MESSAGE CHANNEL
    @verified_email_required
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
        
        
    ############################USER IS TYPPING
    @verified_email_required
    def writting(self, data):
        content = {
           'command': 'is_writting',
           'message': data
        }
        self.send_chat_message(content)

         
    ######################ALL COMMANDS
    commands = {
            'fetch_messages':fetch_messages,
            'new_message':new_message,
            'is_writting':writting,
        }     
              
    @verified_email_required
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

        

  
