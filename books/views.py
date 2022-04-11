from django.forms import NullBooleanField
from django.shortcuts import redirect, render
from like.models import LikeModel
from books.models import BookRentByUser, BookReview, BooksModel
from bookstore.models import BookStoreModel
from chat.models import ChatRoom
from core.services import image_upload
from users.models import UserModel


def main(request):
    if request.method == 'GET':
        # 로그인 했을 때
        user = request.user.is_authenticated
        if user:
            # 로그인한 유저와 같은 지역의 서점 불러오기
            user = request.user
            pk_list = []
            # print('내지역>>', user.location)
            local_list = list(UserModel.objects.filter(location=user.location))
            for local in local_list:
                pk_list.append(local.pk)
            stores = BookStoreModel.objects.filter(
                user__in=pk_list).order_by('-created_at')
            # 로그인한 유저와 같은 지역의 책들 불러오기
            books = BooksModel.objects.filter(
                user__in=pk_list).order_by('-created_at')

            context = {
                'stores': stores,
                'books': books
            }
            return render(request, 'bookstore/main.html', context)
        else:
            # 서점 불러오기
            stores = BookStoreModel.objects.all()
            # 책 불러오기
            books = BooksModel.objects.all()

            context = {
                'stores': stores,
                'books': books
            }
            return render(request, 'bookstore/main.html', context)

# 스토어페이지에서 책 클릭하면 디테일 페이지로 이동


def detail(request, book_pk):

    book = BooksModel.objects.get(pk=book_pk)
    buyer = ChatRoom.objects.filter(participants=request.user.pk)
    rented_info = BookRentByUser.objects.filter(book_id=book_pk)
    like_exists = LikeModel.objects.filter(
        user=request.user.id, book=book.id).exists()

    # 해당책후기 가져오기
    reviews = BookReview.objects.filter(book_id=book_pk)

    # 도서정보수정
    if 'status_edit' in request.POST:
        # print('>>>',len(request.FILES.getlist('book_img')))
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
        'reviews': reviews,
        'like_exists': like_exists
    }

    return render(request, 'bookstore/detail.html', context)


def review(request, book_pk):
    try:
        book = BooksModel.objects.get(pk=book_pk)
        reviews = BookReview.objects.get(
            book_id=book_pk, writer_id=request.user.pk)
    except BookReview.DoesNotExist:

        # 리뷰작성

        if 'write_review' in request.POST:
            review = BookReview.objects.create(
                content=request.POST['content'],
                review_rating=request.POST['review_rating'],
                writer_id=request.user.id,
                book_id=book_pk
            )
            return redirect('my-page')
        return render(request, 'users/review.html', {'book': book})

    # 리뷰수정
    if 'edit_review' in request.POST:
        reviews.content = request.POST['content']
        reviews.review_rating = request.POST['review_rating']
        reviews.save()

        return redirect('my-page')

    return render(request, 'users/review.html', {'book': book, 'reviews': reviews})
