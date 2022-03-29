from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from like.models import LikeModel
from books.models import BooksModel
from core.services import image_upload
from users.models import UserModel


def user_username_update(id, username):
    user = UserModel.objects.get(id=id)
    exists_user = UserModel.objects.filter(username=username).exists()
    if user.username == username:
        return
    if exists_user:
        return '이미 사용하고 있는 유저가 있습니다'
    user.username = username
    user.save()
    return


def user_password_update(id, password, password2):
    if password == password2:
        user = get_user_model().objects.get(id=id)
        user.set_password(password)
        user.save()
        return
    elif password != password2:
        error = '잘못된 비밀번호입니다. 다시 확인해주세요.'
        return error


def upload_user_image(file, id):
    url = image_upload('users', file, id)
    user = UserModel.objects.get(id=id)
    user.user_image = url
    user.save()
    return


def get_my_book_list(user_id, offset, limit):
    return BooksModel.objects.filter(user_id=user_id).order_by("-id").prefetch_related(
        Prefetch("like", queryset=LikeModel.objects.filter(
            user_id=user_id), to_attr="my_likes")
    )[offset: offset + limit]
