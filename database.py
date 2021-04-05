import sqlite3

def run_query(sql, params = ()):

    #grab data from DB
    db = sqlite3.connect('chinook.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result