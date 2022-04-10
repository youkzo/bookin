from chat.services import find_new_message_in_chat_rooms_with_user


def new_message_exist_renderer(request):
    if request.user.is_authenticated:
        return {
            'user_new_message_exists': find_new_message_in_chat_rooms_with_user(request.user.id),
        }
    else:
        return {}
