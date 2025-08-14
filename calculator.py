from tkinter import *

cal = Tk()
cal.title("calculator ✨")
cal.geometry("444x444")
cal.config(bg="crimson")

def plus():
    a = float(ent1.get())
    b = float(ent2.get())
    result.config(text=a + b)

def minus():
    a = float(ent1.get())
    b = float(ent2.get())
    result.config(text=a - b)

def mul():
    a = float(ent1.get())
    b = float(ent2.get())
    result.config(text=a * b)

def div():
    a = float(ent1.get())
    b = float(ent2.get())
    if b != 0:
        result.config(text=a / b)
    else:
        result.config(text="تقسیم بر صفر")

Label(cal, text= "frist number:", bg="dark gray", fg="black").pack()
ent1 = Entry(cal)
ent1.pack()

Label(cal, text=" second number:", bg="dark gray", fg="black").pack()
ent2 = Entry(cal)
ent2.pack()

Button(cal, text="+", bg="yellow", command=plus).pack(pady=5)
Button(cal, text="-", bg="pink", command=minus).pack(pady=5)
Button(cal, text="*", bg="light green", command=mul).pack(pady=5)
Button(cal, text="/", bg="blue", command=div).pack(pady=5)

result = Label(cal, text="result", bg="dark gray", fg="black",)
result.pack(pady=10)

