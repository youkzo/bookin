from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('book/detail/<int:book_pk>', views.detail, name='detail'),
    path('books/review/<int:book_pk>', views.review, name='review'),
]
