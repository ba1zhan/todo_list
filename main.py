from db import main_db
import flet as ft



def main(page: ft.Page):
    # print('hello flet')
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=25)

    filter_type = 'all'

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text in main_db.get_tasks(filter_type):
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task_text))


    def view_tasks(task_id, task_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)

        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
            else:
                task_field.read_only = True

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True

        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        def delete_task(_):
            main_db.delete_task(task_id=task_id)
            task_list.controls.remove(task_row)
            task_list.update()

        delete_button = ft.IconButton(icon=ft.Icons.DELETE_FOREVER_OUTLINED,icon_color=ft.Colors.RED,on_click=delete_task)

        task_row = ft.Row([task_field, edit_button, save_button, delete_button])
        return task_row
    
    def toggle_task(task_id, is_completed):
        print(is_completed)
        main_db.update_task(task_id=task_id, completed=int(is_completed))
        load_tasks()
    
    
    def add_task_db(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task=task)
            print(f'Задача {task} добавлена! Его ID - {task_id}')
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task))
            task_input.value = None

    task_input = ft.TextField(label="Введите задачу:", expand=True, on_submit=add_task_db)
    task_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task_db)

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_tasks()


    filter_buttons = ft.Row([
        ft.ElevatedButton('Все задачи', on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX, icon_color=ft.Colors.BLACK),
        ft.ElevatedButton('В работе', on_click=lambda e: set_filter('uncompleted'), icon=ft.Icons.WATCH_LATER, icon_color=ft.Colors.RED),
        ft.ElevatedButton('Готово', on_click=lambda e: set_filter('completed'), icon=ft.Icons.CHECK_BOX, icon_color=ft.Colors.GREEN)
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    send_task = ft.Row([task_input, task_button])

    page.add(send_task, task_list)
    load_tasks()


if __name__ == '__main__':
    main_db.init_db()
    ft.run(main, view=ft.AppView.WEB_BROWSER)