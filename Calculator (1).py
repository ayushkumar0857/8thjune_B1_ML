import tkinter as y

expr = " "

app = y.Tk()
app.title('Basic Calculator')
app.geometry('270x335')
app.configure(background='black')

result = y.Variable(app)
y.Entry(app, textvariable=result, width=32).place(x=30,y=40)

def total():
    global expr
    result.set(eval(expr))
    expr=" "

def clearScreen():
    global expr
    expr=" "
    result.set(expr)

def values(num):
    global expr
    expr = expr+num
    result.set(expr)

y.Button(app, text='Clear', width = 5, height=1, command=lambda: clearScreen(),bg='blue').place(x=20,y=5)

y.Button(app, text='7', width = 5, height=2, command=lambda: values('7'),bg='orange',foreground='white').place(x=30,y=70)
y.Button(app, text='8', width = 5, height=2, command=lambda: values('8'),bg='orange',foreground='white').place(x=80,y=70)
y.Button(app, text='9', width = 5, height=2, command=lambda: values('9'),bg='orange',foreground='white').place(x=130,y=70)
y.Button(app, text='/', width = 5, height=2, command=lambda: values('/'),bg='purple',foreground='white').place(x=180,y=70)

y.Button(app, text='4', width = 5, height=2, command=lambda: values('4'),bg='orange',foreground='white').place(x=30,y=140)
y.Button(app, text='5', width = 5, height=2, command=lambda: values('5'),bg='orange',foreground='white').place(x=80,y=140)
y.Button(app, text='6', width = 5, height=2, command=lambda: values('6'),bg='orange',foreground='white').place(x=130,y=140)
y.Button(app, text='*', width = 5, height=2, command=lambda: values('*'),bg='purple',foreground='white' ).place(x=180,y=140)

y.Button(app, text='1', width = 5, height=2, command=lambda: values('1'),bg='orange',foreground='white').place(x=30,y=210)
y.Button(app, text='2', width = 5, height=2, command=lambda: values('2'),bg='orange',foreground='white').place(x=80,y=210)
y.Button(app, text='3', width = 5, height=2, command=lambda: values('3'),bg='orange',foreground='white').place(x=130,y=210)
y.Button(app, text='-', width = 5, height=2, command=lambda: values('-'),bg='purple',foreground='white').place(x=180,y=210)

y.Button(app, text='.', width = 5, height=2, command=lambda: values('.'),bg='orange',foreground='white').place(x=30,y=280)
y.Button(app, text='0', width = 5, height=2, command=lambda: values('0'),bg='orange',foreground='white').place(x=80,y=280)
y.Button(app, text='=', width = 5, height=2, command=lambda: total(),bg='red',foreground='white').place(x=130,y=280)
y.Button(app, text='+', width = 5, height=2, command=lambda: values('+'),bg='purple',foreground='white').place(x=180,y=280)

app.mainloop()
