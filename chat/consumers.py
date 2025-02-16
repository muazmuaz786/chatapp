import json
from channels.generic.websocket import AsyncWebsocketConsumer  # 비동기 WebSocket 처리를 위한 기본 클래스
from urllib.parse import parse_qs


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        query_params = parse_qs(self.scope["query_string"].decode())
        self.username = query_params.get("username", ["익명"])[0]
        self.room_group_name = query_params.get("group", ["chat"])[0]

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": f"{self.username} has entered.",
                "sender": "system",
            }
        )


    async def disconnect(self, code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": f"{self.username} has left",
                "sender": "system"
            }
        )

    
    async def receive(self, text_data):
        data = json.loads(text_data)  # JSON 데이터로 변환
        message = data.get('message')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                "sender": self.username
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        sender = event.get("sender", "system")  # sender가 없으면 system으로 설정

        # WebSocket을 통해 메시지를 클라이언트로 전달
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender
        }))