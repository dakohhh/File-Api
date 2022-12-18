
from database import conn, cursor
from exceptions.custom_execption import DatabaseException



async def _upload_file(file_id, filename, content_type, user_id):
    try:
        sql = "INSERT INTO files(file_id, file_name, content_type, user_id) VALUES(%s, %s, %s, %s)"
        val = (file_id, filename, content_type, user_id, )
        cursor.execute(sql, val)
        conn.commit()
    except:
        raise DatabaseException


    
def _file(file_id):
    try:
        sql = "SELECT * from files WHERE file_id=%s"
        val = (file_id, )
        cursor.execute(sql, val)
        result = cursor.fetchall()
        
        if result:
            return result
    except:
        raise DatabaseException


async def _get_all_files(user_id):
    try:
        sql = "SELECT * from files WHERE user_id=%s"
        val = (user_id, )
        cursor.execute(sql, val)
        result = cursor.fetchall()

        files = {}

        if result:
            for i in range(1, len(result) + 1):files[i] =  {"file_id": result[i-1][0],"file_name": result[i-1][1],"date_uploaded": str(result[i-1][4])}

            return files
    
    except:
        raise DatabaseException
    


def _delete_file(file_id):
    sql ="DELETE FROM files WHERE file_id=%s"
    val = (file_id, )
    cursor.execute(sql, val)

    
def does_file_exist(file_id):
    sql = "SELECT file_id from files WHERE file_id=%s"
    val = (file_id, )

    cursor.execute(sql, val)

    if cursor.fetchone():
        return True