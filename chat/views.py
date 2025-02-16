from django.shortcuts import render

def chat_login(request):
    return render(request, 'chat_login.html')

def chat_room(request, group, username):
    return render(request, 'chat_room.html', {'group': group, 'username': username})