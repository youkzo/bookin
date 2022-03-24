from django.db import models

from core.models import BaseModel


class LikeModel(BaseModel):
    class Meta:
        db_table = "like"

    user_id = models.ForeignKey(
        'users.UserModel', related_name="like", on_delete=models.CASCADE)

    book_id = models.ForeignKey(
        'books.BooksModel', related_name="like", on_delete=models.CASCADE)
