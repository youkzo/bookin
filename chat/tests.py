from django.test import TestCase

from chat.services import go_chat_room, my_chat_rooms_load
from users.models import UserModel


class ChatTest(TestCase):
    def test_go_chat_room(self):
        # Given
        user_1 = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        user_2 = UserModel.objects.create(
            username='test2', email='test2@12.com', password='test2')

        # When
        chat_room = go_chat_room(user_1.id, user_2.username)

        # Then
        self.assertEqual(2, chat_room.participants.all().count())

    def test_my_chat_rooms_load(self):
        # Given
        user_1 = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        user_2 = UserModel.objects.create(
            username='test2', email='test2@12.com', password='test2')
        go_chat_room(user_1.id, user_2.username)

        # When
        user_1_chat_room_list = my_chat_rooms_load(user_1.id)
        user_2_chat_room_list = my_chat_rooms_load(user_2.id)

        # Then
        self.assertEqual(1, len(user_1_chat_room_list))
        self.assertEqual(1, len(user_2_chat_room_list))
