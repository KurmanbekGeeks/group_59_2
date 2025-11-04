import flet as ft 


def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text(value='Hello world')

    name_input = ft.TextField(label='Введите имя')

    input_button = ft.ElevatedButton(text='send ✅', icon=ft.Icons.SEND_TIME_EXTENSION, color=ft.Colors.PINK_400, icon_color=ft.Colors.GREEN)

    input_button_text = ft.TextButton(text='send', icon=ft.Icons.SEND_ROUNDED)

    input_button_icon = ft.IconButton(icon=ft.Icons.SEND, icon_color=ft.Colors.BROWN)

    page.add(greeting_text, name_input, input_button, input_button_text, input_button_icon)

ft.app(target=main_page)
