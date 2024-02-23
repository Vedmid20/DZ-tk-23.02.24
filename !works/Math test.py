Быстрый доступ к нужным файлам … На новой главной странице показаны самые релевантные файлы и папки.
flet math.txt
import flet as ft
import random
import time

diyaLVL1 = ['+', '-']
diyaLVL2 = ['+', '-', '*', '/']
equation = []
eq = ''
res = ''
complete_eq_lvl1 = 0
complete_eq_lvl2 = 0
complete_eq_all = 0
not_complete_eq_all = 0



def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_resizable = False
    page.window_full_screen = False
    page.window_center()
    page.title = 'Test math skills'
    page.bgcolor = 'indigo300'
    page.window_width = 450
    page.window_height = 350
    t = ft.Text('Enter result', size=30, font_family='SimSun')
    page.update()

    def exit(e):
        page.window_destroy()

    def dark_theme(e):
        page.bgcolor = 'indigo900'
        page.update()

    def light_theme(e):
        page.bgcolor = 'indigo300'
        page.update()

    def settings(e):
        page.clean()
        page.add(ft.Row([
            ft.ElevatedButton(text='Dark theme', width=175, height=45, color='indigo400', bgcolor='white', on_click=dark_theme),
        ], alignment=ft.MainAxisAlignment.CENTER))
        page.add(ft.Row([
            ft.ElevatedButton(text='Light theme', width=175, height=45, color='indigo400', bgcolor='white', on_click=light_theme),
        ], alignment=ft.MainAxisAlignment.CENTER))
        page.add(ft.Row([
            ft.ElevatedButton(text='Back', width=175, height=45, color='indigo400', bgcolor='white', on_click=more),
        ], alignment=ft.MainAxisAlignment.CENTER))

    def statistics(e):
        page.clean()


    def more(e):
        page.clean()
        page.add(ft.Row([
            ft.ElevatedButton(text='Settings', width=175, height=45, color='indigo400', bgcolor='white', on_click=settings),
        ], alignment=ft.MainAxisAlignment.CENTER))
        page.add(ft.Row([
            ft.ElevatedButton(text='Statistic', width=175, height=45, color='indigo400', bgcolor='white', on_click=statistics),
        ], alignment=ft.MainAxisAlignment.CENTER))
        page.add(ft.Row([
            ft.ElevatedButton(text='Back', width=175, height=45, color='indigo400', bgcolor='white', on_click=home),
        ], alignment=ft.MainAxisAlignment.CENTER))

    def home(e):
        page.clean()
        page.add(ft.Row([
            ft.ElevatedButton('Level Easy', on_click=lvl1, width=175, height=45, color='indigo400', bgcolor='white')
        ], alignment=ft.MainAxisAlignment.CENTER))
        page.add(ft.Row([
            ft.ElevatedButton('Level Hard', on_click=lvl2, width=175, height=45, color='indigo400', bgcolor='white')
        ], alignment=ft.MainAxisAlignment.CENTER))
        page.add(ft.Row([
            ft.ElevatedButton('More', width=83, height=40, color='indigo400', bgcolor='white', on_click=more),
            ft.ElevatedButton('Exit', width=83, height=40, color='indigo400', bgcolor='white', on_click=exit),
        ], alignment=ft.MainAxisAlignment.CENTER))

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
            global res, complete_eq_lvl1, complete_eq_all, not_complete_eq_all
            if_result_true = ['Greate!', 'Good!', 'Cool!', 'Amazing!']
            full_res = eval(res)
            if str(inputResult.value) == str(full_res):
                print(full_res)
                complete_eq_lvl1 += 1
                complete_eq_all += 1
                with open('statistics.txt', 'w', encoding='utf-8') as file:
                    file.write(f'Виконані вирази лвл1:{complete_eq_lvl1}\nВиконані вирази all:{complete_eq_all}')
                inputResult.label = 'Result true'
                random_if_result_true = random.choice(if_result_true)
                page.update()
                time.sleep(1.3)
                page.clean()
                page.add(ft.Row([
                    ft.Text(f'{random_if_result_true}', size=55, color='white')
                ], alignment = ft.MainAxisAlignment.CENTER))
                page.update()
                time.sleep(1)
                lvl1(e)

            else:
                inputResult.label = 'Result not true'
                not_complete_eq_all += 1
                with open('statistics_not_cpt_eq.txt', 'w', encoding='utf-8') as file:
                    file.write(f'Не розвязані вирази: {not_complete_eq_all}')
                print(full_res)
            page.update()

        page.add(ft.Row([
            inputResult,
            ft.ElevatedButton(text='Done', bgcolor='white', color='indigo400', width=100, height=45, on_click=result)
        ]))
        page.add(ft.Row([
            ft.ElevatedButton(text='Home', bgcolor='white', color='indigo400', width=200, height=35, on_click=home),
            ft.ElevatedButton(text='New equation', bgcolor='white', color='indigo400', width=200, height=35,
            on_click=lvl1)
        ]))

        page.update()

    def lvl2(e):
        global random_length, eq, res
        page.clean()
        equation.clear()
        eq = ''
        page.update()
        random_length = random.randint(2, 4)
        x = 0
        while x != random_length:
            x += 1
            random_num = random.randint(1, 200)
            random_diya = random.choice(diyaLVL2)
            random_num = str(random_num)
            equation.append(random_num)
            equation.append(random_diya)
        for i in equation:
            eq += str(i)
        if eq.endswith('-') or eq.endswith('+') or eq.endswith('*') or eq.endswith('/'):
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
            full_res1 = int(full_res).__round__(1)
            if str(inputResult.value) == str(full_res1):
                print(full_res1)
                inputResult.label = 'Result true'
                random_if_result_true = random.choice(if_result_true)
                page.update()
                time.sleep(1.3)
                page.clean()
                page.add(ft.Row([
                    ft.Text(f'{random_if_result_true}', size=55, color='white')
                ], alignment = ft.MainAxisAlignment.CENTER))
                page.update()
                time.sleep(1)
                lvl2(e)

            else:
                inputResult.label = 'Result not true'
                print(full_res1)
            page.update()

        page.add(ft.Row([
            inputResult,
            ft.ElevatedButton(text='Done', bgcolor='white', color='indigo400', width=100, height=45, on_click=result)
        ]))
        page.add(ft.Row([
            ft.ElevatedButton(text='Home', bgcolor='white', color='indigo400', width=200, height=35, on_click=home),
            ft.ElevatedButton(text='New equation', bgcolor='white', color='indigo400', width=200, height=35,
            on_click=lvl2)
        ]))

        page.update()


    page.add(ft.Row([
        ft.ElevatedButton('Level Easy', on_click=lvl1, width=175, height=45, color='indigo400', bgcolor='white')
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([
        ft.ElevatedButton('Level Hard', on_click=lvl2, width=175, height=45, color='indigo400', bgcolor='white')
    ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([
        ft.ElevatedButton('More', width=83, height=40, color='indigo400', bgcolor='white', on_click=more),
        ft.ElevatedButton('Exit', width=83, height=40, color='indigo400', bgcolor='white', on_click=exit),
    ], alignment=ft.MainAxisAlignment.CENTER))


if __name__ == '__main__':
    ft.app(target=main)
