import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChessGameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"game_{self.room_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print(f"🟢 Connected to {self.room_group_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"🔴 Disconnected from {self.room_group_name}")

    async def receive(self, text_data):
        data = json.loads(text_data)

        if data.get("type") == "resign":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'resign_event',
                    'username': data.get('username')
                }
            )
        elif data.get("move"):
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'send_move',
                    'move': data['move'],
                    'username': data['username']
                }
            )
    async def resign_event(self, event):
        await self.send(text_data=json.dumps({
            'type': 'resign',
            'username': event['username']
        }))


    async def send_move(self, event):
        await self.send(text_data=json.dumps({
            'move': event['move'],
            'username': event['username']
        }))
