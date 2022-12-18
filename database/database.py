import mysql.connector
import string
import random




conn = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "wisdom",
    database= "wishare"
)

cursor = conn.cursor()



