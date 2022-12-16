import os
import jwt
import datetime
from dotenv import load_dotenv


load_dotenv()

def getToken(user_id:str):
    token = jwt.encode(
        {"user":user_id, 
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
        }, os.getenv("ADMIN_SECRET_KEY"))
    
    return token




def decodeToken(token):
    try:
        data = jwt.decode(token, os.getenv("ADMIN_SECRET_KEY"), algorithms=["HS256"])
        return data
    except:
        return False
    






