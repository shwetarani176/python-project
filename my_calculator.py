from tkinter import *

from tkinter import ttk
def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnCear():
    global val
    val=""
    data.set("")
def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)

root = Tk()
root.geometry("361x381+500+200")
#background color
#root.configure(bg="black")

root.title("Calculator")
val=""
data=StringVar()
#input box creation here
display=Entry(root,textvariable=data,justify="right",bd=29,bg="powder blue" ,font=("Arial",20,"bold"))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(9))
btn9.grid(row=1,column=2)
btnadd=Button(root,text="+",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick("+"))
btnadd.grid(row=1,column=3)


btn4=Button(root,text="4",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(6))
btn6.grid(row=2,column=2)
btnsub=Button(root,text="-",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick("-"))
btnsub.grid(row=2,column=3)

btn1=Button(root,text="1",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(3))
btn3.grid(row=3,column=2)
btnmul=Button(root,text="*",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick("*"))
btnmul.grid(row=3,column=3)

btnc=Button(root,text="C",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnCear())
btnc.grid(row=4,column=0)
btn0=Button(root,text="0",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick(0))
btn0.grid(row=4,column=1)
btndiv=Button(root,text="%",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnClick("/"))
btndiv.grid(row=4,column=3)
btnequal=Button(root,text="=",bd=10 ,width=6,height=2,font=("Arial",12,"bold"),command=lambda :btnEqual())
btnequal.grid(row=4,column=2)
#titlelabel= Label(frame1,text="Calculator",font=("Arial",20),bg="white",borderwidth=1,relief="solid",highlightbackground="black",highlightcolor="black",highlightthickness=2)
#titlelabel.pack()
'''
frame0=Frame(root)
frame0.pack()

button1=Button(frame0,text="C",bd=0 ,width=18,height=2,relief=RAISED,borderwidth=2,font=("solid",10))


button1.grid(row=0,column=0)

button1=Button(frame0,text="/",width=18,height=2,relief=RAISED,borderwidth=2,font=("Ariel",10,"bold"))

button1.grid(row=0,column=1)


frame2=Frame(root)
frame2.pack()
#we create grid or button
#tic toc board

#first row
button1=Button(frame2,text="7" ,width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=0)

button1=Button(frame2,text="8",width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=1)

button1=Button(frame2,text="9",width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))
button1.grid(row=0,column=2)

button1=Button(frame2,text="*",width=10,height=2,relief=RAISED,borderwidth=2,font=("solid",10))
button1.grid(row=0,column=3)

frame3=Frame(root)
frame3.pack()
#second row
button1=Button(frame3,text="4" ,width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=0)

button1=Button(frame3,text="5",width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=1)

button1=Button(frame3,text="6",width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))
button1.grid(row=0,column=2)

button1=Button(frame3,text="-",width=10,height=2,relief=RAISED,borderwidth=2,font=("solid",10))
button1.grid(row=0,column=3)

frame4=Frame(root)
frame4.pack()


#third row
button1=Button(frame4,text="1" ,width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=0)

button1=Button(frame4,text="2",width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=1)

button1=Button(frame4,text="3",width=8,height=2,relief=RAISED,borderwidth=2,font=("solid",10))
button1.grid(row=0,column=2)

button1=Button(frame4,text="+",width=10,height=2,relief=RAISED,borderwidth=2,font=("solid",10))
button1.grid(row=0,column=3)

frame5=Frame(root)
frame5.pack()
#second row
button1=Button(frame5,text="0" ,width=12,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=0)

button1=Button(frame5,text="●",width=12,height=2,relief=RAISED,borderwidth=2,font=("solid",10))

button1.grid(row=0,column=1)

button1=Button(frame5,text="=",width=11,height=2,relief=RAISED,borderwidth=2,font=("solid",10))
button1.grid(row=0,column=2)

'''


root.mainloop()

