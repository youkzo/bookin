from django.test import TestCase
from chat.models import ChatRoom

from chat.services import create_message, find_new_message_in_chat_rooms_with_user, go_chat_room, my_chat_rooms_load
from users.models import UserModel


class ChatTest(TestCase):
    def test_go_chat_room(self):
        # Given
        user_1 = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        user_2 = UserModel.objects.create(
            username='test2', email='test2@12.com', password='test2')

        # When
        chat_room = go_chat_room(user_1.username, user_2.username)

        # Then
        self.assertEqual(2, chat_room.participants.all().count())

    def test_my_chat_rooms_load(self):
        # Given
        user_1 = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        user_2 = UserModel.objects.create(
            username='test2', email='test2@12.com', password='test2')
        go_chat_room(user_1.username, user_2.username)

        # When
        user_1_chat_room_list = my_chat_rooms_load(user_1.id)
        user_2_chat_room_list = my_chat_rooms_load(user_2.id)

        # Then
        self.assertEqual(1, len(user_1_chat_room_list))
        self.assertEqual(1, len(user_2_chat_room_list))

    def test_chat_room_has_new_message(self):
        # Given
        user_1 = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        user_2 = UserModel.objects.create(
            username='test2', email='test2@12.com', password='test2')
        test_chat_room = go_chat_room(user_1.username, user_2.username)

        # When
        create_message(user_1, test_chat_room.id, 'test')

        # Then
        self.assertEqual(True, ChatRoom.exist_new_message(
            test_chat_room, user_2.id))

    def test_user_read_message(self):
        # Given
        user_1 = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        user_2 = UserModel.objects.create(
            username='test2', email='test2@12.com', password='test2')
        test_chat_room = go_chat_room(user_1.username, user_2.username)
        create_message(user_1, test_chat_room.id, 'test')
        create_message(user_2, test_chat_room.id, 'test')

        # When
        ChatRoom.read_messages(test_chat_room, user_2.id)

        # Then
        self.assertEqual(False, ChatRoom.exist_new_message(
            test_chat_room, user_2.id))

    def test_find_new_message_in_chat_rooms_with_user(self):
        # Given
        user_1 = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        user_2 = UserModel.objects.create(
            username='test2', email='test2@12.com', password='test2')
        test_chat_room = go_chat_room(user_1.username, user_2.username)

        # When
        create_message(user_1, test_chat_room.id, 'test')

        # Then
        self.assertEqual(
            True, find_new_message_in_chat_rooms_with_user(user_2.id))
        self.assertEqual(
            False, find_new_message_in_chat_rooms_with_user(user_1.id))
