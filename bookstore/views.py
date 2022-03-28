import datetime
from django.shortcuts import redirect, render
from books.models import BooksModel

from bookstore.models import BookStoreModel
from users.models import UserModel


def mystore(request, pk):
    print('pk', pk)
    # 스토어에 데이터가 있는 경우
    try:
        # 로그인한 유저의 스토어정보 & 업로드한 도서정보
        owner = BookStoreModel.objects.get(user_id=pk)
        books = BooksModel.objects.filter(user_id=pk)

        #도서 업로드
        if 'books_upload' in request.POST:
            # 체크박스 체크/해제 여부
            is_rent = len(request.POST.getlist('is_rent'))
            print(is_rent)
            if is_rent == 1:
                status = True
            else:
                status = False

            add_book = BooksModel.objects.create(
                updated_at=datetime.date.today(),
                created_at=datetime.date.today(),
                book_name=request.POST['book_name'],
                price=request.POST['price'],
                content=request.POST['content'],
                rating=request.POST['rating'],
                book_img=request.POST['book_img'],
                category=request.POST['category'],
                is_rent=status,
                # book_views = request.POST['book_views'],
                store_id=owner.pk,
                user_id=pk,
            )
            # 로그인한 유저의 마이스토어로 redirect
            return redirect('mystore', owner.user.pk)
        
        elif 'store_info_edit' in request.POST:
            owner.store_name = request.POST['store_name']
            owner.store_info = request.POST['store_info']
            owner.store_img = request.POST['store_img']
            owner.save()
            
            return redirect('mystore', owner.user.pk)
            
            #스토어에 데이터가 없는 경우(에러메시지+스토어등록)

    except BookStoreModel.DoesNotExist:
        if 'store_register' in request.POST:
            print('mystore.store.register')
            store_register = BookStoreModel.objects.create(
                updated_at=datetime.date.today(),
                created_at=datetime.date.today(),
                store_name=request.POST['store_name'],
                store_info=request.POST['store_info'],
                store_img=request.POST['store_img'],
                store_views=request.POST['store_views'],
                user_id=pk,
            )
            return redirect('mystore', store_register.pk)

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


def detail(request, book_pk):
    book = BooksModel.objects.get(pk=book_pk)
    return render(request, 'bookstore/detail.html', {'book': book})

