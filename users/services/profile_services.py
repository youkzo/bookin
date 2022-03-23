from django.contrib.auth import get_user_model
from core.services import image_upload
from users.models import UserModel


def user_username_update(id, username):
    user = UserModel.objects.get(id=id)
    user.username = username
    user.save()
    return


def user_password_update(id, password):
    user = get_user_model().objects.get(id=id)
    user.set_password(password)
    user.save()
    return user


def upload_user_image(file, id):
    url = image_upload('users', file, id)
    user = UserModel.objects.get(id=id)
    user.user_image = url
    user.save()
    return
