from users.models import UserModel


def create_an_user(email, username, password):
    return UserModel.objects.create_user(email=email, username=username, password=password)
