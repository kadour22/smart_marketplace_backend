from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("🔌 WebSocket connect called")
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        print("✅ WebSocket connected")

    async def disconnect(self, close_code):
        print(f"❌ WebSocket disconnected: {close_code}")
        await self.channel_layer.group_discard("notifications", self.channel_name)