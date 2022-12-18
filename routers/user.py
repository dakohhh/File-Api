from fastapi import APIRouter, Form
from auth_jwt import getToken
from auth_user import authenticate
from func import create_user, does_email_exist, get_user_id
from starlette.status import HTTP_200_OK
from response.response import customResponse
from exceptions.custom_execption import UserExistExecption, UnauthorizedExecption, ServerErrorException


user = APIRouter(
    prefix="/api",
    tags=""
)




@user.post("/signup")
async def signup(fullname=Form(), email= Form(), password= Form()):
    if does_email_exist(email):
        raise UserExistExecption("Email already exists")
    
    result = create_user(fullname, email, password)
    
    if result: return customResponse(
            HTTP_200_OK, 
            "Account created", 
            data=getToken(get_user_id(email))
            )
    else:
        raise ServerErrorException("Server Error")



@user.post("/request_token")
async def request_token(email:str = Form(), password:str=Form()):
    user = authenticate(email, password)
    if not user:
        raise UnauthorizedExecption("Incorrect email or password")

    return customResponse(
        HTTP_200_OK, 
        "Token created", 
        data=getToken(get_user_id(email))
    )