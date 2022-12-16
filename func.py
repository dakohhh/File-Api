import string
import random
from database import conn, cursor
from authentication.auth_pass import hashPassword




def generate_id(lenght:int):
    result = ""
    for i in range(0, lenght):
        result = result +random.choice(string.ascii_letters)
    
    if does_id_exist(result):
        return generate_id(lenght)
    else:
        return result
    

def does_email_exist(email):

    sql = "SELECT email FROM users WHERE email = %s"

    cursor.execute(sql, (email, ))

    if cursor.fetchone():
        return True


def does_id_exist(id):
    
    sql = "SELECT user_id FROM users WHERE user_id = %s"

    cursor.execute(sql, (id, ))

    if cursor.fetchone():
        return True





def create_user(fullname , email, password):

    sql = "INSERT INTO users(user_id, full_name, email, password, verification_id) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(sql, (generate_id(6), fullname, email, hashPassword(password), generate_id(30), ))

    conn.commit()


def get_user_id(email):
    try:
        sql = "SELECT user_id FROM users WHERE email=%s"
        cursor.execute(sql, (email, ))

        return cursor.fetchone()[0]
    except:raise Exception


def does_vid_exist(id:str):
    sql = "SELECT user_id FROM users WHERE verification_id = %s"
    cursor.execute(sql, (id, ))

    return cursor.fetchone()




def verify_user(user_id:str):
    sql = "UPDATE users SET verified = TRUE WHERE user_id=%s"
    cursor.execute(sql, (user_id, ))

    conn.commit()

async def is_user_verified(email:str):
    sql = "SELECT verified FROM users WHERE email=%s"
    cursor.execute(sql, (email, ))

    return cursor.fetchone()[0]



async def get_vid(email:str):
    sql = "SELECT verification_id FROM users WHERE email =%s"
    cursor.execute(sql, (email, ))

    return cursor.fetchone()[0]












    

    