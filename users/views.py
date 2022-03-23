
from django.shortcuts import redirect
from django.shortcuts import render, redirect

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

        error = create_an_user(email, username, password, password2)
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
        if user:
            return render(request, 'users/profile.html')
        else:
            return redirect("/")
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username != "" and username != request.user.username:
            user_username_update(request.user.id, username)
        if password:
            user = user_password_update(request.user.id, password)

        return redirect('/my-page')


def user_image_post(request):
    file = request.FILES['file']
    upload_user_image(file, request.user.id)
    return redirect('/my-page')
