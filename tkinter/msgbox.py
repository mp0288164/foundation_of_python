from tkinter import *
from tkinter import messagebox
def calc():
    messagebox.showwarning('warning','hellow message')
top=Tk()
b=Button(top,text='click me',command=calc)
b.place(x=30,y=70)
top.geometry("200x200")
#top.minimize('100x100')
top.mainloop()