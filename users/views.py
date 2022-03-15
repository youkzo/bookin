import os
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.views import View
from users.models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import string
import random


def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        # password가 다를 때
        if password != password2:
            return render(request, 'users/signup.html', {'error': '잘못된 비밀번호입니다. 다시 확인하세요.'})
        else:
            if username == '' or password == '' or email == '':
                return render(request, 'users/signup.html', {'error': '사용자 이름과 비밀번호를 입력해 주세요.'})

            exist_user = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'users/signup.html', {'error': '사용자가 이미 존재합니다.'})
            else:
                UserModel.objects.create_user(
                    username=username, email=email, password=password
                )
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, email=email, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'users/signin.html', {'error': '이메일 혹은 패스워드를 확인해주세요.'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'users/signin.html')
