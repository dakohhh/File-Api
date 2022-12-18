import os
from fastapi.responses import JSONResponse, FileResponse


def customResponse(status, msg , success=True, data=None,):

    return JSONResponse(
        status_code=status,
        content={
        "status":status,
        "msg": msg,
        "success": success,
        "data": data if data != None else None
        }
    )



def CustomFileResponse(file_info):
    file_path = os.path.join(os.getcwd(), f"upload\{file_info[0][0]}")
    

    return FileResponse(
		path=file_path,
		filename=file_info[0][1], 
		media_type=file_info[0][2])
    




