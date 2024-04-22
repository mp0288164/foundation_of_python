from tkinter import *
from tkinter import tkk 
def obtain():
    if int(combo.get())>=18:
        txtsel.sel("value"+combo.get()+"greater or equal to 18")
    else:
        txtsel.sel("value"+combo.get()+"lesstane or equal to 18")
root=tk()
txtsel=stringvar()
textsel.set("Answer")
combo=ttk.combobox(root)
combo.place(x=50,y=100)
combo["value"]=('13','34','67','90','18')
combo.current(3)
btn=Button(root,text='calculate',command=obtain)
btn.place(x=80,y=100)
label=Label(root,textvariable=txtsel).place(x=40,y=200)
root.geometry("400X300")
root.mainloop()