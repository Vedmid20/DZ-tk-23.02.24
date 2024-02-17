import tkinter

root = tkinter.Tk()
w = root.winfo_screenwidth() / 2 - 150
h = root.winfo_screenheight() / 2 - 150
root.geometry(f'300x300+{int(w)}+{int(h)}')
root.wm_resizable(width=False,height=False)
x = 0
root.title('0')
t = tkinter.Label(root, text='Hello world!', fg='sea green', font=(None, 30))
t.pack(ipady=20)

def change_text():
    global t, x
    x += 1
    root.title(str(x))
    if x % 2 == 0:
        t.config(text='Hello world!')
    else:
        t.config(text='This is tkinter!')


btn = tkinter.Button(root, text='Change text', background='brown2', borderwidth=3, command=change_text, relief='ridge', activebackground='firebrick3')
btn.pack(ipadx = 10, ipady = 10)
root.mainloop()