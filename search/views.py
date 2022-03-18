from django.shortcuts import redirect, render

from search.services import search_book_and_bookstore


def search_all(request, search_word):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            books, bookstores = search_book_and_bookstore(search_word)
            return render(request, 'search/search_main.html', {'books': books, 'bookstores': bookstores})
