import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "companies.db")

with sqlite3.connect(db_path) as db:
    cursor = db.cursor()

    #resposta_db = db.execute('Select * from Equipment_Details')
    #cursor.execute("INSERT INTO teste VALUES('Luciano', 5)")
    # print(resposta_db)
