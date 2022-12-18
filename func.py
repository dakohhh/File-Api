import string
import random
from database import conn, cursor
from auth_pass import hashPassword, checkPassword




def generate_id():
    result = "W"
    for i in range(0, 6):
        result = result +random.choice(string.ascii_letters)
    
    if does_id_exist(result):
        return generate_id()
    else:
        return result
    

def does_email_exist(email):
    try:

        sql = "SELECT email FROM users WHERE email = %s"

        cursor.execute(sql, (email, ))

        if cursor.fetchone():
            return True
    except:
        raise Exception


def does_id_exist(id):
    
    sql = "SELECT user_id FROM users WHERE user_id = %s"

    cursor.execute(sql, (id, ))

    if cursor.fetchone():
        return True





def create_user(fullname , email, password):
    try:
        sql = "INSERT INTO users(user_id, full_name, email, password) VALUES(%s, %s, %s, %s)"
        cursor.execute(sql, (generate_id(), fullname, email, hashPassword(password), ))

        conn.commit()
        return True
    except:
        return False


def get_user_id(email):
    try:
        sql = "SELECT user_id FROM users WHERE email=%s"
        cursor.execute(sql, (email, ))

        return cursor.fetchone()[0]
    except:raise Exception




    



