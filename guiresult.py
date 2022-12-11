from tkinter import*
win=Tk()
win.title("MARKSHEET")
win.geometry("600x600")
win.config(background='blue')

def press():
    x=a.get()+b.get()+c.get()+d.get()+e.get()
    z=f.set(x)
    y=x/5    
    if y<=100 and y>=70:
        h.set('Grade A')
    elif y<=70 and y>=60:
        h.set('Grade B')
    elif y<=60 and y>=45:
        h.set('Grade C') 
    else:
        h.set('You are Fail')
    m=g.set(y)






l1=Label(win,text="REPORT CARD",font='classic 14 italic',bg='green',bd='10',fg='white')
l1.pack()



a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
e=IntVar()
f=IntVar()
g=IntVar()
h=StringVar()





marks1=Label(win,text='Maths')
marks1.place(x=10,y=70)
marks2=Label(win,text='Chemistry')
marks2.place(x=10,y=140)
marks3=Label(win,text='Physics')
marks3.place(x=10,y=210)
marks4=Label(win,text='English')
marks4.place(x=10,y=280)
marks5=Label(win,text='Hindi')
marks5.place(x=10,y=350)


e1=Entry(win,textvariable=a)
e1.place(x=70,y=70)
e1=Entry(win,textvariable=b)
e1.place(x=80,y=140)
e1=Entry(win,textvariable=c)
e1.place(x=70,y=210)
e1=Entry(win,textvariable=d)
e1.place(x=70,y=280)
e1=Entry(win,textvariable=e)
e1.place(x=70,y=350)

#total

total=Button(win,text='Total =',command=press)
total.place(x=10,y=420)
total=Entry(win,textvariable=f)
total.place(x=70,y=420)

#percentage
Percentage=Label(win,text='Percentage =')
Percentage.place(x=10,y=490)
Percentage=Entry(win,textvariable=g)
Percentage.place(x=100,y=490)

#grade
grade=Label(win,text='Grade =')
grade.place(x=10,y=560)
grade=Entry(win,textvariable=h)
grade.place(x=100,y=560)



win.mainloop()