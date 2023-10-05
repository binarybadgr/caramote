import sqlite3

conn = sqlite3.connect('count_rec.db')
cursor = conn.cursor()


# table for store record after done counting in `main.py`
cursor.execute("""
                CREATE TABLE IF NOT EXISTS count_rec (
                ID        INTEGER PRIMARY KEY,
                total     INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
               """)


def write_record(result):
    cursor.execute("""
                INSERT INTO count_rec (result)
                VALUE (?)
                   """, (result,))
    conn.commit()


def get_record():
    cursor.execute("""
                SELECT * FROM count_rec
                   """)
    return cursor.fetchall()
