from ninja import Schema


class UserCreateResponse(Schema):
    is_created: bool
