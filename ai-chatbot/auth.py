import bcrypt


def hash_password(password):
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def create_user(name, email, password):
    password_hash = hash_password(password)

    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

    cursor = connection.cursor()

    query = """
        INSERT INTO users (name, email, password_hash)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, email, password_hash))

    connection.commit()

    cursor.close()
    connection.close()
