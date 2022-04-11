from django.test import TestCase
from books.models import BooksModel
from bookstore.models import BookStoreModel
from search.services import search_book_and_bookstore

from users.models import UserModel


class TestSearch(TestCase):
    def test_search_book_and_bookstore(self):
        # Given
        test_user = UserModel.objects.create(
            username='test1', email='test1@12.com', password='test1')
        test_store = BookStoreModel.objects.create(
            user=test_user, store_name='store', store_info='test')
        test_book = BooksModel.objects.create(
            user=test_user, store=test_store, book_name='test', price=1000, content='test', category='test')

        # When
        book, store = search_book_and_bookstore('test')

        # Then
        self.assertEqual(test_book, book[0])
        self.assertEqual(1, len(store))
