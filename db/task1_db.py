# import sqlite3
# from datetime import datetime

# def get_connection():
#     return sqlite3.connect()

# def init_db():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS tasks(
#                    id INTEGER PRIMARY KEY,
#                    text TEXT,
#                    created TEXT
#                    )
# ''')
# conn.commit()
# conn.close()



# def load_tasks():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECET id, text, created FROM tasks ORDER BY id")
#     result = cursor.fetchall()
#     conn.close
#     return result


# def add_task(task):
