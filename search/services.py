from django.db.models import Q

from books.models import BooksModel
from bookstore.models import BookStoreModel


def search_book_and_bookstore(word):
    books = BooksModel.objects.filter(book_name__contains=word)

    bookStores = set(BookStoreModel.objects.filter(
        Q(books__in=[x for x in books]) | Q(store_name__contains=word) | Q(store_info__contains=word)))
    return (books, bookStores)
