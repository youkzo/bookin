from django.shortcuts import redirect

from users.models import UserModel

from .models import ChatRoom


def go_chat_room(store_user_id, request_user_username):
    user_one = UserModel.objects.filter(id=store_user_id).get()
    user_two = UserModel.objects.filter(username=request_user_username).get()
    if user_one is not None and user_two is not None:
        try:
            chat_room = ChatRoom.objects.filter(
                participants__in=[user_one, user_two])[0]
        except ChatRoom.DoesNotExist:
            chat_room = ChatRoom.objects.create()
            chat_room.participants.add(user_one, user_two)
        return chat_room


def my_chat_rooms_load(store_user_id):
    user = UserModel.objects.filter(id=store_user_id).get()
    if user is not None:
        chatRooms = ChatRoom.objects.filter(participants=user)
        return chatRooms
