from django.shortcuts import render

from bookstore.models import BookStoreModel
from users.models import UserModel

# Create your views here.

def main(request):
    stores = BookStoreModel.objects.all()
    return render(request, 'bookstore/main.html', {'stores':stores})

def detail(request, user_pk):
    owner = UserModel.objects.get(pk=user_pk)
    store = BookStoreModel.objects.get(pk=user_pk)
    return render(request, 'bookstore/store.html', {'owner':owner, 'store':store})
