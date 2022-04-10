from django.db import models

from core.models import BaseModel
from typing import List, Any


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
    book_img = models.CharField(
        max_length=255, default='https://bookin-bucket.s3.ap-northeast-2.amazonaws.com/static/bookin_default.jpg')
    category = models.CharField(max_length=255)
    book_views = models.IntegerField(default=0)
    is_rented = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    my_likes: List[Any]

    def __str__(self):
        return self.book_name


class BookRentByUser(BaseModel):
    user_rented = models.ForeignKey(
        "users.UserModel", related_name="rent", on_delete=models.CASCADE)
    book = models.ForeignKey(
        "BooksModel", related_name="rent", on_delete=models.CASCADE)
    exp_date = models.DateField(null=True)


class BookReview(BaseModel):
    content = models.TextField()
    review_rating = models.IntegerField(default=0)
    writer = models.ForeignKey(
        "users.UserModel", related_name="review", on_delete=models.CASCADE)
    book = models.ForeignKey(
        "BooksModel", related_name="review", on_delete=models.CASCADE)
