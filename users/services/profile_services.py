
from core.services import image_upload
from users.models import UserModel


def update_user(username):
    pass


def reset_password():
    pass


def change_password():
    pass


def upload_user_image(file, id):
    url = image_upload('users', file, id)
    user = UserModel.objects.get(id=id)
    user.user_image = url
    user.save()

    return
