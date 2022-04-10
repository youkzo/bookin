import datetime

from users.models import UserModel

from .models import ChatRoom, Message


def user_read_message_in_room(user, chat_room_id):
    current_user = UserModel.objects.filter(username=user).get()
    current_chat_room = ChatRoom.objects.filter(id=chat_room_id).get()
    ChatRoom.read_messages(current_chat_room, current_user.id)


def go_chat_room(request_user_username, chat_user_username):
    user_one = UserModel.objects.filter(username=request_user_username).first()
    user_two = UserModel.objects.filter(username=chat_user_username).first()
    if user_one is not None and user_two is not None:
        try:
            chat_room = ChatRoom.objects.filter(
                participants=user_one).filter(participants=user_two).get()
            chat_room.read_messages(user_one.id)
        except ChatRoom.DoesNotExist:
            chat_room = ChatRoom.objects.create()
            chat_room.participants.add(user_one, user_two)
        return chat_room


def my_chat_rooms_load(user_id):
    user = UserModel.objects.filter(id=user_id).get()
    if user is not None:
        chatRooms = ChatRoom.objects.filter(
            participants=user).order_by("-updated_at")
        return chatRooms


def create_message(user, chat_room_id, message):
    current_chat_room = ChatRoom.objects.filter(id=chat_room_id).get()
    message = Message.objects.create(
        user=user, chat_room=current_chat_room, message=message)
    current_chat_room.updated_at = datetime.datetime.now()
    current_chat_room.save()
    return datetime.datetime.now()


def find_new_message_in_chat_rooms_with_user(user_id):
    chatRooms = my_chat_rooms_load(user_id)
    for chatRoom in chatRooms:
        if chatRoom.exist_new_message(user_id):
            return True
    return False
