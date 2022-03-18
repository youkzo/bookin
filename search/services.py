from books.models import BooksModel
from bookstore.models import BookStoreModel


def search_book_and_bookstore(word):
    books = BooksModel.objects.filter(book_name__contains=word)
    bookStores = BookStoreModel.objects.filter(books__in=books)
    return (books, bookStores)
