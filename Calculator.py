from tkinter import *

equa = ''

def btnPress(num) :
	global equa
	equa = equa + str(num)
	equation.set(equa)

def calc() :
	global equa
	c=equa.replace('^','**')
	soln = str(eval(c))
	equation.set(soln)
	equa = ''

def clr() :
	equation.set('')
	global equa
	equa = ''

def del_one():
	global equa
	equa = equa[:-1]
	equation.set(equa)

root = Tk()
root.minsize(200,200)
root.maxsize(400,400)

# Creating dynamic variable
equation = StringVar()
equation.set('Enter your equation :')
#Creating Label

calculation = Label(root,textvariable = equation)

calculation.grid(row=0,columnspan=4)

#Creating Buttons

Btn1 = Button(root, text = '1' , width = 5, command = lambda : btnPress(1))
Btn1.grid(row = 1, column = 0)

Btn2 = Button(root, text = '2', width = 5, command = lambda : btnPress(2))
Btn2.grid(row = 1, column = 1 )

Btn3 = Button(root, text = '3', width = 5, command = lambda : btnPress(3))
Btn3.grid(row = 1 , column = 2)

Btn4 = Button(root, text = '4' , width = 5, command = lambda : btnPress(4))
Btn4.grid(row = 2, column = 0)

Btn5 = Button(root, text = '5', width = 5, command = lambda : btnPress(5))
Btn5.grid(row = 2, column = 1 )

Btn6 = Button(root, text = '6', width = 5, command = lambda : btnPress(6))
Btn6.grid(row = 2 , column = 2)

Btn7 = Button(root, text = '7' , width = 5, command = lambda : btnPress(7))
Btn7.grid(row = 3, column = 0)

Btn8 = Button(root, text = '8', width = 5, command = lambda : btnPress(8))
Btn8.grid(row = 3, column = 1 )

Btn9 = Button(root, text = '9', width = 5, command = lambda : btnPress(9))
Btn9.grid(row = 3 , column = 2)

addBtn = Button(root , text = '+' , width = 5, command = lambda : btnPress('+'))
addBtn.grid(row = 1 , column =3)

subBtn = Button(root , text = '-' , width = 5, command = lambda : btnPress('-'))
subBtn.grid(row = 2, column = 3)

mulBtn = Button(root , text = '*' , width = 5, command = lambda : btnPress('*'))
mulBtn.grid(row = 3, column = 3)

divBtn = Button(root, text = '/', width = 5, command = lambda : btnPress('/'))
divBtn.grid(row = 4, column = 3)

Btn0 = Button(root , text ='0' , width = 5, command = lambda : btnPress(0))
Btn0.grid(row = 4,column = 1)

Btnequ = Button(root , text = '=' , width = 5, command = calc )
Btnequ.grid(row = 4, column = 2)

Btnclr = Button(root, text='C', width = 5, command = clr)
Btnclr.grid(row = 4, column = 0)

Btndot = Button(root, text='.', width = 5, command = lambda : btnPress('.'))
Btndot.grid(row = 1, column = 4)

Btndel = Button(root, text='X', width = 5, command = del_one)
Btndel.grid(row = 2, column = 4)

Btn_par_left = Button(root, text='(', width = 5, command = lambda : btnPress('('))
Btn_par_left.grid(row = 3, column = 4)

Btn_par_right = Button(root, text=')', width = 5, command = lambda : btnPress(')'))
Btn_par_right.grid(row = 4, column = 4)

Btn_pow = Button(root, text='^', width = 5, command = lambda : btnPress('^'))
Btn_pow.grid(row = 1, column = 5)


root.mainloop()
