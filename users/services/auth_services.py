from users.models import UserModel

from django.contrib.auth import get_user_model


def create_an_user(email, username, password, password2):
    error = None
    exist_user = get_user_model().objects.filter(email=email).exists()
    if password != password2:
        error = '잘못된 비밀번호입니다. 다시 확인하세요.'
    if username == '' or password == '' or email == '':
        error = '사용자 이름과 비밀번호를 입력해 주세요.'
    if exist_user:
        error = '사용자가 이미 존재합니다.'
    if error:
        return error
    else:
        UserModel.objects.create_user(
            username=username, email=email, password=password)
        return error
