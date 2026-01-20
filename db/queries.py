# C-R-U-D

tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOInCREMENT,
        task TEXT NOT NULL
    )
"""

# Create - создание записи
insert_task = 'INSERT INTO tasks (task) VALUES(?)'


# Read - просмотр записей
select_task = 'SELECT id, task FROM tasks'

# Update - обновить запись
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

# Delete - удаление записи
delete_task = 'DELETE FROM tasks WHERE id = ?'