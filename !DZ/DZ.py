import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = 'User Data'
    page.window_width = 345
    page.window_height = 470
    page.window_resizable = False
    page.theme_mode = 'dark'
    t = ft.Text(value='Enter your data', size=30)
    name = ft.TextField(label='Name', width=310, height=50)
    year = ft.TextField(label='Year', width=150, height=50)
    month = ft.TextField(label='Month', width=150, height=50)
    successfullyTXT = ft.Text(value='', size=15, color='green')


    def result():
        if str(month.value) != '' and year.value != '' and name.value != '':
            with open('file.txt', 'a', encoding='utf-8') as file:
                file.write(f'Name: {name.value.title()}\nYear: {year.value}\nMonth: {month.value}\n-------------\n')
                successfullyTXT.value = 'Successfully'
        else:
            pass

    def validate_month():
        try:
            if int(month.value) <= 12 and int(month.value) >= 1:
                month.border_color = 'green'
                month.label = 'Month'
                result()
            else:
                month.border_color = 'red'
                month.label = 'Error'
        except ValueError:
            month.border_color = 'red'
            month.label = 'Error'
        page.update()

    def validate_year():
      try:
          if  len(year.value) >= 1 and int(year.value) >= 5 and int(year.value) <= 120:
              year.border_color = 'green'
              year.label = 'Year'
              validate_month()
          else:
              year.border_color = 'red'
              year.label = 'Error'
              validate_month()
      except ValueError:
          year.border_color = 'red'
          year.label = 'Error'
          validate_month()
      page.update()

    def validate(e):
        try:
            if len(str(name.value)) >= 2:
                name.border_color = 'green'
                name.label = 'Name'
                validate_year()

            else:
                name.border_color = 'red'
                name.label = 'Error'
                validate_year()

        except ValueError:
            name.border_color = 'red'
            name.label = 'Error'
            validate_year()
        page.update()

    page.add(ft.Row([
        t
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(
        ft.Row(
            [
                ft.Column([name])], alignment=ft.MainAxisAlignment.CENTER))

    page.add(
        ft.Row(
            [
                year,
                month
            ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([
        successfullyTXT
    ]))

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(text='Accept', on_click=validate, width=140, height=40, color='white', bgcolor='grey800')
            ], alignment=ft.MainAxisAlignment.CENTER))

    page.update()


if __name__ == '__main__':
    ft.app(target=main)