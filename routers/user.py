from fastapi import APIRouter, Form
from authentication.auth_jwt import getToken
from authentication.auth_user import authenticate
from func import create_user, does_email_exist, get_user_id, does_vid_exist, verify_user, is_user_verified, get_vid
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
    
    try:
        create_user(fullname, email, password)
    
    
        return customResponse(
                HTTP_200_OK, 
                "Account created, please verify account", 
                data= {"verification_id": await get_vid(email)}
                )
    except:
        raise ServerErrorException("Server Error")



@user.post("/request_token")
async def request_token(email:str = Form(), password:str=Form()):
    user = authenticate(email, password)
    if not user:
        raise UnauthorizedExecption("Incorrect email or password")

    if not await is_user_verified(email):
        raise UnauthorizedExecption("User is not verified, please verify account")
    

    return customResponse(
        HTTP_200_OK, 
        "Token created", 
        data=getToken(get_user_id(email))
    )


@user.post("/verify_account")
async def verify_account(id:str):
    user = does_vid_exist(id)
    if not user:
        raise UnauthorizedExecption("Cannot Verify")
    

    verify_user(user[0])

    return customResponse(HTTP_200_OK, "Account Verified")
    
    
    