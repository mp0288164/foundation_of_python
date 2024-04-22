from tkinter import *
def new():
    print("newfile")
def open():
    print("openfile")
def save():
    print("save file")
def about():
    print("about")
def cut():
    print("cut")
def copy():
    print("copy")

root=Tk()
menu=Menu(root)
filemenu=Menu(menu,tearoff=0)
filemenu.add_command(label='new',command="new")
filemenu.add_command(label='open',command="open")
filemenu.add_separator()
filemenu.add_command(label='about',command="about")
filemenu.add_separator()
filemenu.add_cascade(label='file',menu=filemenu)
root.config(menu=menu)
root.geometry("300x300")
root.configure(bg="pink")
root.mainloop()