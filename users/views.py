
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from books.models import BookRentByUser
from users.services.auth_services import reset_passowrd
from users.services.auth_services import check_email_code
from users.services.auth_services import send_email_auth_code

from users.models import UserModel
from django.contrib import auth

from users.services.auth_services import create_an_user
from users.services.profile_services import upload_user_image, user_password_update, user_username_update


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'users/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        location = request.POST.get('location', '')

        error = create_an_user(email, username, password, password2, location)
        if error:
            return render(request, 'users/signup.html', {'error': error})
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


def logout(request):
    auth.logout(request)
    return redirect("/sign-in")


def delete_user(request):
    auth.logout(request)
    user = UserModel.objects.filter(id=request.user.id).get()
    user.delete()
    return redirect("/")


def my_profile_page(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        # 빌린책후기&별점
        # rentuser = BookRentByUser.objects.filter(book_id=book_pk)
        rented_books = BookRentByUser.objects.filter(
            user_rented_id=request.user.pk)

        if user:
            return render(request, 'users/profile.html', {'rented_books': rented_books})
        else:
            return redirect("/")
    elif request.method == 'POST':
        message = ''
        username = request.POST.get('username', None)
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if username != "":
            user_message = user_username_update(request.user.id, username)
        if user_message:
            return render(request, 'users/profile.html', {'message': user_message})
        if password:
            pw_message = user_password_update(
                request.user.id, password, password2)
        else:
            return redirect("/my-page")
        if pw_message:
            return render(request, 'users/profile.html', {'error': pw_message})
        return redirect("/my-page")


def user_image_post(request):
    file = request.FILES['file']
    upload_user_image(file, request.user.id)
    return redirect('/my-page')


def email_authentication_view(request):
    if request.method == 'GET':
        return render(request, 'users/find_password.html')
    if request.method == 'POST':
        email_code = request.POST.get('email', '')

        authentication_message = send_email_auth_code(email_code)
        if authentication_message:
            return render(request, 'users/find_password.html', {'error': authentication_message})

        response = redirect('/check-password')
        response.set_cookie('email', email_code)
        return response


def email_check_code_view(request):
    email = request.COOKIES['email']
    if request.method == 'GET':
        return render(request, 'users/check-password.html')
    if request.method == 'POST':
        code = request.POST.get('code', '')
        check_email_message = check_email_code(email, code)
        if check_email_message:
            return render(request, 'users/check-password.html', {'error': check_email_message})
        return redirect('/reset-password')


def reset_password_view(request):
    email = request.COOKIES['email']
    if request.method == 'GET':
        return render(request, 'users/reset-password.html')

    if request.method == 'POST':
        new_password = request.POST.get('new_password', '')
        new_password2 = request.POST.get('new_password2', '')

        if new_password != new_password2:
            return render(request, 'users/reset-password.html', {'error': '잘못된 비밀번호입니다. 다시 확인해주세요'})
        else:
            reset_passowrd(email, new_password)
            response = redirect('/sign-in')
            response.delete_cookie('email')
            return response
