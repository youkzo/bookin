from django.forms import NullBooleanField
from django.shortcuts import redirect, render

from books.models import BookRentByUser, BookReview, BooksModel
from bookstore.models import BookStoreModel
from chat.models import ChatRoom
from core.services import image_upload


def main(request):
    stores = BookStoreModel.objects.all()
    return render(request, 'bookstore/main.html', {'stores': stores})

# 스토어페이지에서 책 클릭하면 디테일 페이지로 이동


def detail(request, book_pk):
    

    book = BooksModel.objects.get(pk=book_pk)
    buyer = ChatRoom.objects.filter(participants=request.user.pk)
    rented_info = BookRentByUser.objects.filter(book_id=book_pk)

    # 해당책후기 가져오기
    reviews = BookReview.objects.filter(book_id=book_pk)

    # 도서정보수정
    if 'status_edit' in request.POST:
        print('>>>',len(request.FILES.getlist('book_img')))
        # try:
        #     if request.POST['is_rent'] == 'on':
        #         status = True
        # except MultiValueDictKeyError:
        #     status = False

        # 도서대여상태 체크박스 체크/해제 여부
        is_rent = len(request.POST.getlist('is_rent'))
        if is_rent == 1:
            status = 0
        else:
            status = 1
        
        if len(request.FILES.getlist('book_img')) == 0:
            img_url = book.book_img
        else:
            img_url = image_upload('books', request.FILES['book_img'], book.pk)

        
        book.book_name = request.POST['book_name']
        book.price = request.POST['price']
        book.content = request.POST['content']
        book.rating = request.POST['rating']     
        book.category = request.POST['category']
        book.is_rented = status
        # img_url = image_upload('books', request.FILES['book_img'], book.pk)
        book.book_img = img_url
        book.save()


        try:
            rented_info = BookRentByUser.objects.create(
                book_id=book.pk,
                user_rented_id=request.POST['user_rented_id'],
                exp_date=request.POST['returnday'],
            )
            return redirect('detail', book.pk)

        except ValueError:
            return redirect('detail', book.pk)

    context = {
        'book': book,
        'buyer': buyer,
        'rented_info': rented_info,
        'reviews': reviews
    }

    return render(request, 'bookstore/detail.html', context)


def review(request, book_pk):
    book = BooksModel.objects.get(pk=book_pk)

    # 리뷰작성
    if request.method == "POST":
        review = BookReview.objects.create(
            content=request.POST['content'],
            review_rating=request.POST['review_rating'],
            writer_id=request.user.pk,
            book_id=book_pk
        )
        return redirect('my-page')

    return render(request, 'bookstore/review.html', {'book': book})
