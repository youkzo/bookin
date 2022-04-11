from django.db import models

from core.models import BaseModel


class Message(BaseModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.UserModel", related_name="messages", on_delete=models.CASCADE)
    chat_room = models.ForeignKey(
        "ChatRoom", related_name="messages", on_delete=models.CASCADE
    )
    is_readed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} : {self.message}"


class ChatRoom(BaseModel):
    participants = models.ManyToManyField(
        "users.UserModel", related_name="chatroom", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def exist_new_message(self, user_id):
        return self.messages.exclude(user_id=user_id).filter(is_readed=False).exists()

    def read_messages(self, user_id):
        self.messages.exclude(user_id=user_id).update(is_readed=True)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"
