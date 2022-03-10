from ninja import Router, Form

from users.apis.v1.schemas.user_create_request import UserCreateRequest
from users.apis.v1.schemas.user_create_response import UserCreateResponse

from users.services.auth_services import (
    create_an_user
)

router = Router(tags=["users"])


@router.post("/sign-up/", response={201: UserCreateResponse})
def create_user(request, user_create_request: UserCreateRequest = Form(...)):
    user = create_an_user(user_create_request.email,
                          user_create_request.username, user_create_request.password)
    return 201, {"is_created": True}
