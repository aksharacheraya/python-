from tkinter import*
root=Tk()
root.title('calculater')
root.geometry("120x360")
root.resizable(False,False)
root.attributes("-topmost",True)
def clicked(num):
    first_num=text.get()
    text.delete(0,END)
    text.insert(0,str(first_num)+str(num))
def add():
    first_number=text.get()
    global old_value
    old_value=int(first_number)
    global math
    math="addition"
    text.delete(0,END)
def sub():
    first_number=text.get()
    global old_value
    old_value=int(first_number)
    global math
    math="sub"
    text.delete(0,END)
def div():
    first_number=text.get()
    global old_value
    old_value=int(first_number)
    global math
    math="div"
    text.delete(0,END)
def mul():
    first_number=text.get()
    global old_value
    old_value=int(first_number)
    global math
    math="mul"
    text.delete(0,END)
def equal():
    if math=="addition":
            new_value=text.get()
            text.delete(0,END)
            text.insert(0,int(old_value)+int(new_value))
    elif math=="sub":
            new_value=text.get()
            text.delete(0,END)
            text.insert(0,int(old_value)-int(new_value))
    elif math=="div":
            new_value=text.get()
            text.delete(0,END)
            text.insert(0,int(old_value)/int(new_value))
    elif math=="mul":
            new_value=text.get()
            text.delete(0,END)
            text.insert(0,int(old_value)*int(new_value))
def clear():
    text.delete(0,END)
btn=Button(root,text=" 1 ",command=lambda:clicked(1))
btn1=Button(root,text=" 2 ",command=lambda:clicked(2))
btn2=Button(root,text=" 3 ",command=lambda:clicked(3))
btn3=Button(root,text=" 4 ",command=lambda:clicked(4))
btn4=Button(root,text=" 5 ",command=lambda:clicked(5))
btn5=Button(root,text=" 6 ",command=lambda:clicked(6))
btn6=Button(root,text=" 7 ",command=lambda:clicked(7))
btn7=Button(root,text=" 8 ",command=lambda:clicked(8))
btn8=Button(root,text=" 9 ",command=lambda:clicked(9))
btn9=Button(root,text=" +/-")
btn10=Button(root,text="  0  ",command=lambda:clicked(0))
btn11=Button(root,text="  . ")
btn12=Button(root,text=" = ", command=equal)
btn13=Button(root,text=" + ",command=add)
btn14=Button(root,text=" - " ,command=sub)
btn15=Button(root,text=" / ",command=div)
btn16=Button(root,text=" * ",command=mul)
btn17=Button(root,text=" b ")
btn18=Button(root,text=" ce ",command=clear)
btn19=Button(root,text=" % ")
labl=Label(root,text="=Standard ")
text=Entry()
btn.place(x=0,y=300)
btn1.place(x=30,y=300)
btn2.place(x=60,y=300)
btn3.place(x=0,y=270)
btn4.place(x=30,y=270)
btn5.place(x=60,y=270)
btn6.place(x=0,y=240)
btn7.place(x=30,y=240)
btn8.place(x=60,y=240)
btn9.place(x=0,y=330)
btn10.place(x=30,y=330)
btn11.place(x=60,y=330)
btn12.place(x=90,y=330)
btn13.place(x=90,y=300)
btn14.place(x=90,y=270)
btn15.place(x=90,y=240)
btn16.place(x=90,y=210)
btn17.place(x=60,y=210)
btn18.place(x=30,y=210)
btn19.place(x=0,y=210)
labl.place(x=3,y=80)
text.place(x=0,width=110,height=100,y=100)

root.mainloop()