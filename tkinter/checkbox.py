from tkinter import *
import tkinter

def sel():
    selection="you selected the option"+str(checkvar1.get())
    label.config(text=selected)
    selection="you selected the option"+str(checkvar2.get())
    Label.config(text=selected)
top=tkinter.Tk()
checkvr1=Intvar()
checkvar2=Intvar()
c1=Checkbutton(top,text='music',variable=checkvar/onvalue=1,offvalue=0,height=5/width=20)
c2=Checkbutton(top,text='vedio',variable=checkvar2/onvalue=1,offvalue=0,height=5/width=20)
c1.pack()
c2.pack()
btn=Button(top,text='calculate',command=sel).place(x=80,y=150)
label1=Label(top)
label1.pack()
label2=Label(top)
label2.pack()
top.mainloop()