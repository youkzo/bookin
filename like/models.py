from django.db import models

from core.models import BaseModel


class LikeModel(BaseModel):
    user = models.ForeignKey(
        'users.UserModel', related_name="like", on_delete=models.CASCADE)
    book = models.ForeignKey(
        'books.BooksModel', related_name="like", on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["user", "book"], name="unique_user_book")]
