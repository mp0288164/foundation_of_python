from tkinter import *
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.place(side=LEFT,fill=X)
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END,"this is line number"+str(line))
mylist.place(side=RIGHT,fill=BOTH)
scrollbar.config(command=mylist.yview)
root.maniloop()