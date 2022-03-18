import datetime
from django.shortcuts import redirect, render
from books.models import BooksModel

from bookstore.models import BookStoreModel
from users.models import UserModel


def store(request, user_pk):
    try:
        owner = UserModel.objects.get(pk=user_pk)
        store = BookStoreModel.objects.get(user_id=user_pk)
        books = BooksModel.objects.filter(user_id=user_pk)
    except BookStoreModel.DoesNotExist:
        return render(request, 'bookstore/store.html', {'owner': owner})

    # 도서업로드시books모델에추가
    if request.method == "POST":
        add_book = BooksModel.objects.create(
            updated_at = datetime.date.today(),
            created_at = datetime.date.today(),
            book_name = request.POST['book_name'],
            rating = request.POST['book_rating'],
            book_img = request.POST['book_img'],
            category = request.POST['category'],
            book_views = request.POST['book_views'],
            store_id = store.id,
            user_id = owner.pk,
        )
        
        return redirect('store', owner.pk)
    
    # 판매도서정보수정(books데이터변경)
    # if request.method == "POST":


    return render(request, 'bookstore/store.html', {'owner': owner, 'store': store, 'books':books})

def detail(request, book_pk):
    book = BooksModel.objects.get(pk=book_pk)
    return render(request, 'bookstore/detail.html', {'book':book})