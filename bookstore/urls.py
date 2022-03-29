from django.urls import path
from . import views

urlpatterns = [
    path('mystore/<int:pk>', views.mystore, name='mystore'),
    path('<int:store_pk>', views.store, name='store'),
]
