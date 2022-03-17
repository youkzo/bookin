from django.urls import path
from . import views

urlpatterns = [
    path('store/<int:user_pk>', views.store, name='store'),
]
