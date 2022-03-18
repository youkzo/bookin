from django.urls import path
from . import views


urlpatterns = [
    path('search/<str:search_word>', views.search_all, name='search-all'),
]
