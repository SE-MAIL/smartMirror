import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class MirrorConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'mirror_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        time = text_data_json['time']
        isOpen = text_data_json['isOpen']
        response = text_data_json['response']


        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'time': time,
                'isOpen': isOpen,
                'response': response
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        time = event['time']
        isOpen = event['isOpen']
        response = event['response']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'time': time,
            'isOpen' : isOpen,
            'response': response
        }))