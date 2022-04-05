from django.test import TestCase
from users.services.auth_services import send_email_auth_code
from users.services.profile_services import get_my_book_list
from like.services.like_service import do_like
from users.services.auth_services import make_email_auth_code
from bookstore.models import BookStoreModel
from books.models import BooksModel
from users.models import UserModel


class TestProfile(TestCase):
    def test_get_book_list_should_prefetch_like(self):
        user = UserModel.objects.create(username="test")
        book_store = BookStoreModel.objects.create(
            user=user, store_name="test_store")
        book = [BooksModel.objects.create(
            user=user, store=book_store, book_name=f"{i}") for i in range(1, 21)]
        do_like(user.id, book[-1].id)
        book_list = get_my_book_list(user.id, 0, 10)

        self.assertEqual(20, book[-1].id)

    # def test_login_user(self):
    #     user = UserModel.objects.create(username="test")

    #     response = self.client.post(
    #         "/sign-in/",
    #         data={
    #             "email": user.email,
    #             "password": user.password,
    #         },
    #         content_type="application/json",
    #     )
    #     print(response.context)
    #     self.assertEqual(200, response.status_code)

    def test_get_my_book_list(self):
        user = UserModel.objects.create(username='test')
        user2 = UserModel.objects.create(
            username='test2', email="test@gmail.com")
        book_store = BookStoreModel.objects.create(
            user=user, store_name="test_store")
        book = [BooksModel.objects.create(
            user=user, store=book_store, book_name=f"{i}") for i in range(1, 21)]
        book = [BooksModel.objects.create(
            user=user2, store=book_store, book_name=f"{i}번") for i in range(1, 21)]

        do_like(user.id, book[0].id)

        my_book = get_my_book_list(user.id, 0, 20)

        self.assertEqual(20, my_book.count())

    def test_make_auth_num(self):
        auth_num = make_email_auth_code()
        print(auth_num)

    def test_send_email(self):
        user = UserModel.objects.create(
            username='test', email='wkddnjsdl00@naver.com')
        send_email_auth_code(user.email)
