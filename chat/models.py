from django.db import models

from core.models import BaseModel


class Message(BaseModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.UserModel", related_name="messages", on_delete=models.CASCADE)
    chat_room = models.ForeignKey(
        "ChatRoom", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"


class ChatRoom(BaseModel):
    participants = models.ManyToManyField(
        "users.UserModel", related_name="chatroom", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"
