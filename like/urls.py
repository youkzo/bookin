from django.urls import path
from . import views


urlpatterns = [
    path('book/detail/like/', views.like_book, name='like_book'),
]
