from django.urls import path
from . import views


urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('my-page/', views.my_profile_page, name='my-page'),
    path('api/upload-user-img', views.update_image, name='upload-user-img'),
]
