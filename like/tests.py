from django.db import IntegrityError
from django.test import TestCase
from like.models import LikeModel
from users.models import UserModel
from books.models import BooksModel
from bookstore.models import BookStoreModel
from like.services.like_service import do_like, undo_like


class TestLikeService(TestCase):
    def test_a_user_can_like_a_book(self):
        # Given
        user = UserModel.objects.create(username="test")
        book_store = BookStoreModel.objects.create(
            user=user, store_name="test_store")
        book = BooksModel.objects.create(
            user=user, store=book_store, book_name="test_name")

        like = do_like(user.id, book.id)

        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(book.id, like.book_id)

    def test_a_user_can_like_a_book_only_once(self):
        user = UserModel.objects.create(username="test")
        book_store = BookStoreModel.objects.create(
            user=user, store_name="test_store")
        book = BooksModel.objects.create(
            user=user, store=book_store, book_name="test_name")

        do_like(user.id, book.id)
        with self.assertRaises(IntegrityError):
            do_like(user.id, book.id)

    def test_like_count_should_increase(self):
        user = UserModel.objects.create(username="test")
        book_store = BookStoreModel.objects.create(
            user=user, store_name="test_store")
        book = BooksModel.objects.create(
            user=user, store=book_store, book_name="test_name")

        do_like(user.id, book.id)

        book = BooksModel.objects.get(id=book.id)

        self.assertEqual(1, book.like_count)

    def test_a_use_can_undo_like(self):
        user = UserModel.objects.create(username="test")
        book_store = BookStoreModel.objects.create(
            user=user, store_name="test_store")
        book = BooksModel.objects.create(
            user=user, store=book_store, book_name="test_name")

        like = do_like(user.id, book.id)

        undo_like(user.id, book.id)

        with self.assertRaises(LikeModel.DoesNotExist):
            LikeModel.objects.filter(id=like.id).get()

    def test_like_delete_when_cascade(self):
        user = UserModel.objects.create(username="test")
        book_store = BookStoreModel.objects.create(
            user=user, store_name="test_store")
        book = BooksModel.objects.create(
            user=user, store=book_store, book_name="test_name")
        like = LikeModel.objects.create(user_id=user.id, book_id=book.id)
        book.delete()

        with self.assertRaises(LikeModel.DoesNotExist):
            LikeModel.objects.get(id=book.id)
