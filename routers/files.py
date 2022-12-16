from typing import Union
from fastapi import APIRouter, File, Header, UploadFile
from authentication.auth_jwt import decodeToken
from starlette.status import HTTP_200_OK
from func import generate_id
from response.response import customResponse
from exceptions.custom_execption import NotFound, UnauthorizedExecption, ServerErrorException



file_route = APIRouter(
    prefix="/api",
    tags=""
)




@file_route.post("/file")
async def upload(x_api_key:Union[str, None] = Header(default=None), file:UploadFile = File(...)):
    user = decodeToken(x_api_key)
    if not user:
        raise UnauthorizedExecption("Invalid Token")

    try:
        data = await file.read()
        file_id = generate_id(6)

        from mutler import Mutler
        from controllers.file import _upload_file
        
        mutler = Mutler("upload")
        await _upload_file(file_id, file.filename,file.content_type, user["user"])
        await mutler.put(file_id, data)

        return customResponse(
            HTTP_200_OK, 
            "Upload successfully",
            data= {"file_id": file_id, "link": f"localhost:8000/file/{file_id}"}
        )
    except:
        raise ServerErrorException("Server Error")



@file_route.get("/file/{file_id}")
async def download(file_id:str, x_api_key:Union[str, None] = Header(default=None)):
	payload = decodeToken(x_api_key)
        
	from controllers.file import _file
	file_info = _file(file_id)
        
        
	if not payload:
		raise UnauthorizedExecption("Invalid Token")
	
	if file_info != []:
		if file_info[0][3] != payload["user"]:
			raise UnauthorizedExecption("User does not have access to this file")
	else:
		raise NotFound("File does not exist with ithis id")

	try:
		from response.response import CustomFileResponse
		return CustomFileResponse(file_info)
	
	except:
		raise ServerErrorException("Server Error")


        

        
@file_route.get("/view_all_files")
async def view_all_files(x_api_key:Union[str, None] = Header(default=None)):
	payload = decodeToken(x_api_key)
	
	if not payload:
		raise UnauthorizedExecption("Invalid Token")
	try:

		from controllers.file import _get_all_files

		files = await _get_all_files(payload["user"])

		return customResponse(HTTP_200_OK, "Get Files successfull", success=True, data=files)
	
	except:
		raise ServerErrorException("Server Error")





@file_route.delete("/file/{file_id}")
def delete(file_id:str, x_api_key:Union[str, None] = Header(default=None)):
	payload = decodeToken(x_api_key)
        
	from controllers.file import _file, _delete_file
	file_info = _file(file_id)
        
        
	if not payload:
		raise UnauthorizedExecption("Invalid Token")
	
	if file_info != []:
		if file_info[0][3] != payload["user"]:
			raise UnauthorizedExecption("User does not have access to this file")
	else:
		raise NotFound("File does not exist with this id")
	
	try:
		_delete_file(file_id)

		return customResponse(HTTP_200_OK, "File deleted successfully")
	except:
		raise ServerErrorException("Server Error")