from django.urls import path  # URL을 설정하기 위해 path 함수 가져옴
from .consumers import ChatConsumer  # WebSocket 처리를 담당할 ChatConsumer 가져옴

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),  # /ws/chat/ URL로 WebSocket 연결을 처리
]