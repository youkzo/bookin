from django.urls import path
from . import views


urlpatterns = [
    path('.well-known/pki-validation/<str:filename>',
         views.pki_validation, name='pki-validation'),
    path('.well-known/<str:filename>', views.validation, name='validation'),
]
