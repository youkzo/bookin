from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('delete-user/', views.delete_user, name='delete-user'),
    path('my-page/', views.my_profile_page, name='my-page'),
    path('api/upload-user-image/', views.user_image_post,
         name='upload-user-image'),
    path('find-password/', views.email_authentication_view,
         name='email-authentication'),
    path('check-password/', views.email_check_code_view,
         name='email-check'),
    path('reset-password/', views.reset_password_view,
         name='reset-password'),
]
