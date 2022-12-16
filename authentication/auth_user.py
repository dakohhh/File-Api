from database import cursor
from func import does_email_exist, get_user_id
from .auth_pass import checkPassword







def authenticate(email:str, password:str):
    if does_email_exist (email):
        sql = "SELECT email, password FROM users WHERE email=%s"
        val = (email, )
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return get_user_id(email) if checkPassword(password, result[0][1]) else False
    else:return False


