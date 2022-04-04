from django.urls import path
from . import views


urlpatterns = [
    path('.well-known/pki-validation/', views.validation, name='pki-validation'),
    path('.well-known/', views.validation, name='validation'),
]
