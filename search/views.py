from django.shortcuts import redirect, render

from search.services import search_book_and_bookstore


def search_all(request):
    if request.method == 'GET':
        search_word = request.GET.get('word')
        books, bookstores = search_book_and_bookstore(search_word)
        return render(request, 'search/search_main.html', {'books': books, 'bookstores': bookstores, 'word': search_word})
