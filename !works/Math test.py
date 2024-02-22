import flet as ft
import random
import time

sqrt = ' **0.5 '
diyaLVL1 = ['+', '-']
diyaLVL2 = ['+', '-', '*', '/']
diyaLVL3 = ['+', '-', '*', '/', sqrt, ]
equation = []
eq = ''
res = ''


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_resizable = False
    page.window_center()

    page.bgcolor = 'indigo300'
    page.window_width = 450
    page.window_height = 350
    t = ft.Text('Enter result', size=30, font_family='SimSun')
    page.update()

    def lvl1(e):
        global random_length, eq, res
        page.clean()
        equation.clear()
        eq = ''
        page.update()
        random_length = random.randint(2, 4)
        x = 0
        while x != random_length:
            x += 1
            random_num = random.randint(1, 150)
            random_diya = random.choice(diyaLVL1)
            random_num = str(random_num)
            equation.append(random_num)
            equation.append(random_diya)
        for i in equation:
            eq += str(i)
        if eq.endswith('-') or eq.endswith('+'):
            res = eq[:-1]
        eq_text = ft.Text(value=res, size=33, color='white')
        inputResult = ft.TextField(label='Enter result', border_color='white', height=45)

        page.add(ft.Row([
            eq_text
        ], alignment=ft.MainAxisAlignment.CENTER
        ))

        def result(e):
            global res
            if_result_true = ['Greate!', 'Good!', 'Cool!', 'Amazing!']
            full_res = eval(res)
            if str(inputResult.value) == str(full_res):
                print(full_res)
                inputResult.label = 'Result true'
                random_if_result_true = random.choice(if_result_true)
                page.update()
                time.sleep(1.3)
                page.clean()
                page.add(ft.Row([
                    ft.Text(f'{random_if_result_true}', size=45, color='white')
                ], alignment = ft.MainAxisAlignment.CENTER))
                page.update()
                time.sleep(1)
                lvl1(e)

            else:
                inputResult.label = 'Result not true'
                print(full_res)
            page.update()

        page.add(ft.Row([
            inputResult,
            ft.ElevatedButton(text='Done', bgcolor='white', color='indigo400', width=100, height=45, on_click=result)
        ]))
        page.add(ft.Row([
            ft.ElevatedButton(text='Home', bgcolor='white', color='indigo400', width=200, height=35,),
            ft.ElevatedButton(text='New equation', bgcolor='white', color='indigo400', width=200, height=35,
            on_click=lvl1)
        ]))

        page.update()

    page.add(ft.Row([
        ft.ElevatedButton('Level Easy', on_click=lvl1, width=150, height=45, color='indigo400', bgcolor='white')
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([
        ft.ElevatedButton('Level Normal', width=150, height=45, color='indigo400', bgcolor='white')
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([
        ft.ElevatedButton('Level Hard', width=150, height=45, color='indigo400', bgcolor='white')
    ], alignment=ft.MainAxisAlignment.CENTER))


if __name__ == '__main__':
    ft.app(target=main)
