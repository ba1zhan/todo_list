# C-R-U-D

tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOInCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
"""

# Create - создание записи
insert_task = 'INSERT INTO tasks (task) VALUES(?)'


# Read - просмотр записей
select_task = 'SELECT id, task, completed FROM tasks'

select_task_completed = 'SELECT id, task, completed FROM  tasks WHERE completed = 1'

select_task_uncompleted = 'SELECT id, task, completed FROM  tasks WHERE completed = 0'

# Update - обновить запись
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

# Delete - удаление записи
delete_task = 'DELETE FROM tasks WHERE id = ?'