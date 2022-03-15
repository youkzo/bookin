from django.contrib import admin

from books.models import BookRentByUser, BooksModel

admin.site.register(BooksModel)
admin.site.register(BookRentByUser)
