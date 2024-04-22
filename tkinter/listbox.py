from tkinter import *
def selection():
    a=Lb1.curselection()
    print(a)
    for i in range():
        print(Lb1.get(i))
    return

top=Tk()
Lb1=Listbox(top,selectmode=EXTENDED)
Lb1.insert(1,"python")
Lb1.insert(2,"java")

Lb1.pack()
b1=Button(top,text="click me",command=selection)
b1.pack()
top.mainloop()
