from django.urls import path
from . import views

urlpatterns = [
    path('mystore/<int:pk>', views.mystore, name='mystore'),
<<<<<<< HEAD
    path('/<int:store_pk>', views.store, name='store'),
=======
    path('<int:store_pk>', views.store, name='store'),
    path('store/detail/<int:book_pk>', views.detail, name='detail'),
>>>>>>> 2384279d2d553f8d041cbe7c0240442a877aeb4d
]
