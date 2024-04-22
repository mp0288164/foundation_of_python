from tkinter import *
from tkinter import messagebox
def calc():
    s=messagebox.askquestion('warning','do you want to save')
    if (s==True):
        messagebox.showinfo('message','press yes')
    else:
        messagebox.showinfo('message','press no')
top=Tk()
b=Button(top,text='click me',command=calc)
b.place(x=30,y=70)
top.geometry("200x200")
#top.minimize('100x100')
top.mainloop()