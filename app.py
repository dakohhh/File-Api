from fastapi import FastAPI
from routers.user import user
from routers.files import file_route
from exceptions.custom_execption import *





app = FastAPI()


app.include_router(user)
app.include_router(file_route)

app.add_exception_handler(UserExistExecption, user_exist_exception_handler)
app.add_exception_handler(UnauthorizedExecption, unauthorized_exception_handler)
app.add_exception_handler(ServerErrorException, server_exception_handler)
app.add_exception_handler(NotFound, not_found_exception_handler)


@app.get("/api")
def home():
    return "Welcome to WISHARE goto /docs for documentation"







