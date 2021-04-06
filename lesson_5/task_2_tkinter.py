import tkinter as tk
from collections import defaultdict


def get_num(num):
    return int(num.get(), 16)


def insert(num):
    num = str(num).replace('0x', '')
    text_answer.delete(0, 'end')
    text_answer.insert(0, num.upper())


def add():
    answer = hex(get_num(text_num1) + get_num(text_num2))
    insert(answer)


def sub():
    answer = hex(get_num(text_num1) - get_num(text_num2))
    insert(answer)


def delete():
    try:
        answer = hex(int(get_num(text_num1) / get_num(text_num2)))
        insert(answer)
    except ZeroDivisionError:
        text_answer.delete(0, 'end')
        text_answer.insert(0, 'NOT VALID DATE')


def mul():
    answer = hex(get_num(text_num1) * get_num(text_num2))
    insert(answer)


root = tk.Tk()
root.geometry('220x270')
root.resizable(0, 0)
root.title('HexNumber')
root.configure(bg="silver")
d = defaultdict(list)

text_num1 = tk.Entry(root, width=20, bg="black", fg="gold")
text_num2 = tk.Entry(root, width=20, bg="black", fg="gold")
text_answer = tk.Entry(root, width=20, bg="black", fg="gold")
label_num1 = tk.Label(root, text="Введите первое число", background="silver")
label_num2 = tk.Label(root, text="Введите второе число", background="silver")
label_answer = tk.Label(root, text="Операция и ответ:", background="silver")

button_add = tk.Button(root, text='+', width=7, command=add, height=2, bg="gold")
button_sub = tk.Button(root, text='-', width=7, command=sub,  height=2, bg="gold")
button_mul = tk.Button(root, text='*', width=7, command=mul,  height=2, bg="gold")
button_div = tk.Button(root, text='/', width=7, command=delete, height=2, bg="gold")

label_num1.place(x=45, y=20)
label_num2.place(x=45, y=61)
label_answer.place(x=45, y=200)
text_num1.place(x=45, y=40)
text_num2.place(x=45, y=81)
button_add.place(x=45, y=110)
button_sub.place(x=110, y=110)
button_mul.place(x=45, y=154)
button_div.place(x=110, y=154)
text_answer.place(x=45, y=221)

root.mainloop()
