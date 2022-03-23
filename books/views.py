from django.shortcuts import render

from bookstore.models import BookStoreModel


def main(request):
    stores = BookStoreModel.objects.all()
    return render(request, 'bookstore/main.html', {'stores': stores})


