import flet as ft 
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text(value='Hello world')
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []
    history_text = ft.Text('История приветствий:')


    def on_button_click(_):
        name = name_input.value.strip()
        # print(name)

        if name:
            greeting_text.color = None
            greeting_text.value = f'Hello {name}'
            name_input.value = None

            # greeting_history.append(timestamp + " " + name)
            timestamp = datetime.now().strftime("%D:%M:%Y  %H:%M:%S")

            greeting_history.append(f"{timestamp} {name}")
            history_text.value = 'История приветствий: \n' + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Вы не ввели имя!'
            greeting_text.color = ft.Colors.RED

        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    input_button_text = ft.TextButton(text='send', icon=ft.Icons.SEND_ROUNDED, on_click=on_button_click)

    def theme_mode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    theme_mode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_mode)


    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()


    clear_button = ft.ElevatedButton(text='Clear', icon=ft.Icons.DELETE, on_click=clear_history)


    page.add(greeting_text, name_input, input_button_text,theme_mode_button, clear_button, history_text)

ft.app(target=main_page)