from django.core.mail import EmailMessage
from users.models import UserModel

from django.contrib.auth import get_user_model
import string
import random


def create_an_user(email, username, password, password2, location):
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
            username=username, email=email, password=password, location=location)
        return error


def make_email_auth_code():
    LENGTH = 8
    string_pool = string.ascii_letters + string.digits
    auth_num = ""
    for i in range(LENGTH):
        auth_num += random.choice(string_pool)
    return auth_num


def send_email_auth_code(email):
    exist_user = UserModel.objects.filter(email=email).exists()
    mail_subject = 'bookin 인증 코드'
    message = make_email_auth_code()
    send_email = EmailMessage(mail_subject, message, to=[email])
    if exist_user:
        UserModel.objects.filter(email=email).update(email_code=message)
        send_email.send()
    else:
        error = '이메일을 확인해주세요.'
        return error


def check_email_code(email, code):
    check_code_in_user = UserModel.objects.filter(
        email=email).values('email_code')
    if code == check_code_in_user[0]['email_code']:
        return
    else:
        error = '잘못된 코드입니다. 다시 입력해주세요.'
        return error


def reset_passowrd(email, password):
    user = UserModel.objects.get(email=email)
    user.set_password(password)
    user.save()
    return
