from django.urls import path
from chat.views import chat_login, chat_room

urlpatterns = [
    path('', chat_login, name='chat_login'),
    path('chat/<str:group>/<str:username>/', chat_room, name='chat_room'),
]