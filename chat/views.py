from django.http import HttpResponse
from django.shortcuts import redirect, render

from chat.services import create_message, go_chat_room, my_chat_rooms_load, user_read_message_in_room


def chat_room_list(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            my_rooms = my_chat_rooms_load(request.user.id)
            return render(request, "chat/chatRoomList.html", {'rooms': my_rooms})
        else:
            return redirect('/')


def chatting_room(request, username):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            my_room = go_chat_room(request.user.username, username)
            return render(request, "chat/chattingRoom.html", {'room': my_room, 'messages': my_room.messages.all().order_by('created_at')})
        else:
            return redirect('/')
    elif request.method == 'POST':
        if 'user' in request.POST:
            user = request.POST.get('user')
            chat_room_id = request.POST.get('chat_room_id')
            user_read_message_in_room(user, chat_room_id)
            return HttpResponse('OK')
        else:
            user = request.user
            message = request.POST.get('message', '')
            chat_room_id = request.POST.get('chat_room_id', '')
            result = create_message(user, chat_room_id, message)
            return HttpResponse(result.strftime("%p %I:%M "))
