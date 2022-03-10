from email.policy import strict
from ninja import Schema


class UserCreateRequest(Schema):
    email: str
    username: str
    password: str
