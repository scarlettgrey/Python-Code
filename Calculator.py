from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)

def equalclick():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

calc = Tk()
calc.geometry("300x160")
equation = StringVar()

expression_field = Entry(calc,textvariable=equation)
expression_field.grid(columnspan = 4, ipadx = 70)


button1 = Button(calc, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7) 
button1.grid(row=2, column=0) 

button2 = Button(calc, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7) 
button2.grid(row=2, column=1) 

button3 = Button(calc, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7) 
button3.grid(row=2, column=2) 

button4 = Button(calc, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7) 
button4.grid(row=3, column=0) 

button5 = Button(calc, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7) 
button5.grid(row=3, column=1) 

button6 = Button(calc, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7) 
button6.grid(row=3, column=2) 

button7 = Button(calc, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7) 
button7.grid(row=4, column=0) 

button8 = Button(calc, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7) 
button8.grid(row=4, column=1) 

button9 = Button(calc, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7) 
button9.grid(row=4, column=2) 

button0 = Button(calc, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7) 
button0.grid(row=5, column=0) 

plus = Button(calc, text=' + ', fg='black', bg='red',  command=lambda: press("+"), height=1, width=7) 
plus.grid(row=2, column=3) 

minus = Button(calc, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7) 
minus.grid(row=3, column=3) 

multiply = Button(calc, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 

divide = Button(calc, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7) 
divide.grid(row=5, column=3) 

equal = Button(calc, text=' = ', fg='black', bg='red', command=equalclick, height=1, width=7) 
equal.grid(row=5, column=2) 

point = Button(calc, text=' , ', fg='black', bg='white', command=lambda: press(","), height=1, width=7)
point.grid(row=5,   column=1)

clear = Button(calc, text='Clear', fg='black', bg='red', command=clear, height=1, width=7) 
clear.grid(row=6, column=1)

calc.mainloop()