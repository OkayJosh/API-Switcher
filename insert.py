import db_connection
import sqlite3
from domain.object import User
from domain.port import UserPort


 # Insert each user's data into the database
def store_data_in_db(users):
    for user in users:
        sqlite3.Cursor.execute('''
            INSERT OR REPLACE INTO users (id, name, age, address, gender, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user['id'], user['name'], user['age'], user['address'], user['gender'], user['email']))