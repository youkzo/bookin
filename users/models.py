from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    user_image = models.CharField(
        max_length=255, default="https://bookin-bucket.s3.ap-northeast-2.amazonaws.com/static/bookin_default.jpg")
    email_code = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
