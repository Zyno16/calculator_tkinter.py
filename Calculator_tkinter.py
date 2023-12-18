import tkinter
from tkinter import ttk

form = tkinter.Tk()
form.geometry("700x300")
fnt =("None 25 bold")
lblnum1 = ttk.Label(form,text = "number1:",font =fnt)
lblnum2 = ttk.Label(form,text = "number2:",font =fnt)

sv1 =tkinter.StringVar()
sv2 =tkinter.StringVar()
txtnum1 =ttk.Entry(form,font =fnt,textvariable =sv1)
txtnum2 =ttk.Entry(form,font =fnt,textvariable =sv2)
sv1.set("0")
sv2.set("0")
lblnum1.grid(row=0,column=0,pady =10,padx =10)
lblnum2.grid(row=1,column=0,pady =10,padx =10)
txtnum1.grid(row =0,column =1)
txtnum2.grid(row=1 ,column =1)

def calc(ope):
    str1 = str(txtnum1.get())
    str2 = str(txtnum2.get())
    n1 = int(str1)
    n2 = int(str2)
    r=0
    if ope == "+":r =n1+n2
    elif ope == "-": r =n1-n2
    elif ope =="*":r =n1*n2
    else:
        if n2==0: n2 =1
        r = n1 / n2
    lblr["text"]=("result:%s %s %s=%s") % (n1,ope,n2,round(r,2))
btns =ttk.Style()
btns.configure("TButton",font =fnt,padding =10)
frame=tkinter.Frame(form)
btn_width =5

lbladd=ttk.Button(frame,text="+",width =btn_width,command =lambda:calc("+"))
lblasub=ttk.Button(frame,text="-",width =btn_width,command =lambda:calc("-"))
lbladev=ttk.Button(frame,text="/",width =btn_width,command =lambda:calc("/"))
lblmulti=ttk.Button(frame,text="*",width =btn_width,command =lambda:calc("*"))

frame.grid(row=2,column=0,columnspan=2)
lbladd.grid(row =0,column=0)
lblasub.grid(row =0,column=1)
lblmulti.grid(row =0,column=2)
lbladev.grid(row =0,column=3)

lblr =ttk.Button(frame,text ="result")
lblr.grid(row=1,column =0,columnspan=4,padx=10)
