import datetime

from django.shortcuts import redirect, render

from books.models import BooksModel
from bookstore.models import BookStoreModel
from core.services import image_upload


def mystore(request, pk):
    if pk != request.user.id:
        return redirect('/')
    # 스토어에 데이터가 있는 경우
    try:
        # 로그인한 유저의 스토어정보 & 업로드한 도서정보 불러오기
        owner = BookStoreModel.objects.get(user_id=pk)
        print('pk:', pk, 'owner.user.pk:',owner.user.pk, 'owner.user_id:', owner.user_id)
        books = BooksModel.objects.filter(user_id=pk).order_by('-created_at')  

        # 도서 업로드
        if 'books_upload' in request.POST:
            # 대여상태 체크박스 체크/해제 여부
            is_rent = len(request.POST.getlist('is_rent'))
            print(is_rent)
            if is_rent == 1:
                status = True
            else:
                status = False

            add_book = BooksModel.objects.create(
                book_name=request.POST['book_name'],
                price=request.POST['price'],
                content=request.POST['content'],
                category=request.POST['category'],
                store_id=owner.pk,
                user_id=pk,
            )
            img_url = image_upload(
                'books', request.FILES['book_img'], add_book.pk)
            add_book.book_img = img_url
            add_book.save()
            # 로그인한 유저의 마이스토어로 redirect
            return redirect('mystore', owner.user.pk)

        # 스토어 정보 수정(팝업)
        elif 'store_info_edit' in request.POST:
            if len(request.FILES.getlist('store_img')) == 0:
                img_url = owner.store_img
            else:
                img_url = image_upload('editedimg', request.FILES['store_img'], owner.pk)


            owner.store_name = request.POST['store_name']
            owner.store_info = request.POST['store_info']
            owner.store_img = img_url
            owner.save()

            return redirect('mystore', owner.user.pk)

    # 스토어에 데이터가 없는 경우(에러메시지+스토어등록버튼 표시)
    except BookStoreModel.DoesNotExist:
        if 'store_register' in request.POST:
            # print('mystore.store.register')
            store_register = BookStoreModel.objects.create(
                store_name=request.POST['store_name'],
                store_info=request.POST['store_info'],
                user_id=pk,
            )
            img_url = image_upload(
                'bookstores', request.FILES['store_img'], store_register.pk)
            store_register.store_img = img_url
            store_register.save()

            return redirect('mystore', pk)

        return render(request, 'bookstore/mystore.html', {'error': '스토어정보가 없습니다'})

    return render(request, 'bookstore/mystore.html', {'owner': owner, 'books': books})

# 메인에서 스토어클릭하면 해당 스토어로 이동


def store(request, store_pk):
    try:
        store = BookStoreModel.objects.get(pk=store_pk)
        books = BooksModel.objects.filter(store_id=store_pk)
    except BookStoreModel.DoesNotExist:
        return render(request, 'bookstore/store.html')

    return render(request, 'bookstore/store.html', {'store': store, 'books': books})
