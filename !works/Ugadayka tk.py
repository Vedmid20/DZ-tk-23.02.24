import tkinter
import random
import tkinter.messagebox
import time


root = tkinter.Tk()
w = root.winfo_screenwidth() / 2 - 200
h = root.winfo_screenheight() / 2 - 150
root.geometry(f'400x300+{int(w)}+{int(h)}')
root.resizable(width=False, height=False)
root.title('Ugadayka')
root['bg'] = 'SlateBlue1'
x = 5
def f():
   try:
       min_num = min_entry.get()
       max_num = max_entry.get()
       if int(min_num) < int(max_num):
           r = random.randint(int(min_num),int(max_num))
           print(r)
           min_entry['state'] = 'disabled'
           max_entry['state'] = 'disabled'
           btn['state'] = 'disabled'
           def true_choice():
               global x
               entry_guess_num1 = entry_guess_num.get()
               if x != 0:
                   if int(entry_guess_num1) < r:
                       tkinter.messagebox.showwarning(message='Загадане число більше')
                       x -= 1
                       tries.config(text=f'Спроби: {x}')
                   elif int(entry_guess_num1) > r:
                       tkinter.messagebox.showwarning(message='Загадане число менше')
                       x -= 1
                       tries.config(text=f'Спроби: {x}')
                   else:
                       tkinter.messagebox.showinfo(message='Ви відгадали число. Вітаємо!')
                       time.sleep(1)
                       answer = tkinter.messagebox.askyesno(message='Бажаєш зіграти ще?')
                       if answer == True:
                           min_entry['state'] = 'normal'
                           max_entry['state'] = 'normal'
                           btn['state'] = 'normal'
                           guess_num.place_forget()
                           entry_guess_num.place_forget()
                           attempt.place_forget()
                           x = 5
                           tries.config(text=f'Спроби: {x}')
                       else:
                           root.destroy()
               else:
                   tkinter.messagebox.showinfo(message='Ви потратили усі 5 спроб. Гру завершено')
                   root.destroy()
           guess_num = tkinter.Label(root, text='Вгадай число:', font=(None, 13), background='SlateBlue1')
           guess_num.place(x = 10, y = 140)
           entry_guess_num = tkinter.Entry(root, width=24)
           entry_guess_num.place(x = 130, y = 143)
           attempt = tkinter.Button(root, text='Спробувати', width=20, height=2, command=true_choice, relief='raised', background='orchid1', activebackground='orchid3')
           attempt.place(x = 130, y = 180)
       else:
           tkinter.messagebox.showwarning(message='Мінмальне число має бути менше за максимальне')
   except ValueError:
           tkinter.messagebox.showerror(message='Введено мають бути тільки числа')
min_value_text = tkinter.Label(root, text='Мінімальна кількість', font=(None, 13), background='SlateBlue1', takefocus=1)
min_value_text.place(x = 10, y = 5)
max_value_text = tkinter.Label(root, text='Максимальна кількість', font=(None, 13), background='SlateBlue1')
max_value_text.place(x = 210, y = 5)
min_entry = tkinter.Entry(root, width=25)
max_entry = tkinter.Entry(root, width=25)
min_entry.place(x = 14, y = 30)
max_entry.place(x = 220, y = 30)
btn = tkinter.Button(root, text='Згенерувати', width=20, height=2, command=f, relief='raised', background='orchid1', activebackground='orchid3')
btn.place(x = 130, y = 60)
tries = tkinter.Label(root, text=f'Спроби: {x}', font=(None, 14), background='SlateBlue1')
tries.place(x = 300, y = 260)


root.mainloop()