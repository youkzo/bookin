from django.db import models

from core.models import BaseModel


class BooksModel(BaseModel):
    class Meta:
        db_table = "books"

    user = models.ForeignKey(
        'users.UserModel', related_name="books", on_delete=models.CASCADE)
    store = models.ForeignKey(
        'bookstore.BookStoreModel', related_name="books", on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    book_img = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    book_views = models.IntegerField(default=0)
    is_rent = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name


class BookRentByUser(BaseModel):
    user_rented = models.ForeignKey(
        "users.UserModel", related_name="rent", on_delete=models.CASCADE)
    book = models.ForeignKey(
        "BooksModel", related_name="rent", on_delete=models.CASCADE)
    exp_date = models.DateField(null=True)
