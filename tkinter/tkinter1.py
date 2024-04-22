from tkinter import *
def sel():
    selection="you selected the option"+str(r1.get()),label.config(text="selection")
root=Tk()
var=IntVar()
r1=Radiobutton(root,text="option1",variable=var,value=5,command=sel)
r1.pack(anchor=E)

r2=Radiobutton(root,text="option2",variable=var,value=3,command=sel)
r2.pack(anchor=E)

r3=Radiobutton(root,text="option3",variable=var,value=4,command=sel)
r3.pack(anchor=E)

label=Label(root)
label.pack()
root.mainloop()
