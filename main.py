import flet as ft 


def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    greeting_text = ft.Text(value='Hello world')

    def on_button_click(_):
        name = name_input.value.strip()
        # print(name)

        if name:
            greeting_text.color = None
            greeting_text.value = f'Hello {name}'
            name_input.value = None
        else:
            greeting_text.value = 'Вы не ввели имя!'
            greeting_text.color = ft.Colors.RED

        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    input_button_text = ft.TextButton(text='send', icon=ft.Icons.SEND_ROUNDED, on_click=on_button_click)


    page.add(greeting_text, name_input, input_button_text)

ft.app(target=main_page)