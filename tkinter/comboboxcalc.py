from tkinter import *
from tkinter import ttk
def calc():
    txtsel=combo.get()
    if txtsel != "":
        try:
            t3.configure(state="normal")
            t3.delete(0,END)
            num1=float(t1.get())
            num2=float(t2.get())
            if txtsel=="add":
                ans=num1+num2
                t3.insert(0,ans)
                t3.configure(state='disabled')
            elif txtsel=="subtract":
                ans=num1-num2
                t3.insert(0,ans)
                t3.configure(state='disabled')
            elif txtsel=="multiply":
                ans=num1*num2
                t3.insert(0,ans)
                t3.configure(state='disabled')
            elif txtsel=="division":
                try:
                    ans=num1/num2
                    t3.insert(0,ans)
                    t3.configure(state='disabled')
                except zeroDivisionError:
                    t3.insert(0,"zerodivisionerror")
        except ValueError:
            t3.insert(0,'value error')
    else:
        t3.insert(0,"select an index")  

root=Tk()
root.title("cmbocalc")
root.configure(bg='red')
combo=ttk.conbox(root)
combo.place(x=50,y=130)
combo['values']=('add','subtract','multiply','division') 
l1=Label(root,text='enter 1`st no:-',bg='blue',fg='yellow')
l1.place(x=20,y=50)
t1=Entry(root,bg='blue',fg='yellow')
t1.place(x=100,y=50)
l2=Label(root,text='enter 2`st no:-',bg='blue',fg='yellow')
l1.place(x=20,y=70)
t2=Entry(root,bg='blue',fg='yellow')
t2.place(x=100,y=70)
l3=Label(root,text='result',bg='blue',fg='yellow')
l3.place(x=20,y=90)
t3=Entry(root,bg='blue',fg='yellow')
t1.place(x=100,y=90)
btn=Button(root,text='calculate',command=calc,bg='blue',fg='yellow').place(x=80,y=170)
root.geometry("300x200")
root.mainloop()
            
            
        