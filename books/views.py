import datetime
from django.shortcuts import redirect, render
import pkg_resources
from books.models import BookRentByUser, BooksModel
from django.utils.datastructures import MultiValueDictKeyError

from bookstore.models import BookStoreModel


def main(request):
    stores = BookStoreModel.objects.all()
    return render(request, 'bookstore/main.html', {'stores': stores})
    
#스토어페이지에서 책 클릭하면 디테일 페이지로 이동
def detail(request, book_pk):
    book = BooksModel.objects.get(pk=book_pk)

    # 도서정보수정
    if 'status_edit' in request.POST:

        # try:
        #     if request.POST['is_rent'] == 'on':
        #         status = True   
        # except MultiValueDictKeyError:
        #     status = False
        
        # 체크박스 체크/해제 여부
        is_rent = len(request.POST.getlist('is_rent'))
        print(is_rent)
        if is_rent == 1:
            status = True
        else:
            status = False

        book.book_name = request.POST['book_name']
        book.price = request.POST['price']
        book.content = request.POST['content']
        book.rating = request.POST['rating']
        book.book_img = request.POST['book_img']
        book.category = request.POST['category']
        book.is_rent = status
        book.save()

        rented_info = BookRentByUser.objects.create(
            updated_at = datetime.date.today(),
            created_at = datetime.date.today(),
            book_id = book.pk,
            user_rented_id = book.user_id,
            exp_date = request.POST['returnday'],
        )
        return redirect('detail', book.pk)


    return render(request, 'bookstore/detail.html', {'book':book})

