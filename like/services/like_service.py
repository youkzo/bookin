from users.models import UserModel
from like.models import LikeModel
from books.models import BooksModel
from django.db.models import F


def do_like(user_id, book_id):
    UserModel.objects.filter(id=user_id).get()
    BooksModel.objects.filter(id=book_id).get()

    like = LikeModel.objects.create(user_id=user_id, book_id=book_id)
    BooksModel.objects.filter(id=book_id).update(like_count=F("like_count")+1)
    return like


def undo_like(user_id, book_id):
    delete_cnt, _ = LikeModel.objects.filter(
        user_id=user_id, book_id=book_id).delete()
    if delete_cnt:
        BooksModel.objects.filter(id=book_id).update(
            like_count=F("like_count")-1)
