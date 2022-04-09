from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from like.services.like_service import do_like, undo_like
from books.models import BooksModel
from like.models import LikeModel


def like_book(request):
    user = request.user
    book = request.POST.get('book_id')
    like = LikeModel.objects.filter(user=user.id, book=book).exists()

    if like:
        undo_like(user.id, book)
        print('싫어요')
    else:
        do_like(user.id, book)
        print('좋아요')
    return JsonResponse({"status": 'Success'})
