import tkinter as tk
from tkinter import ttk
from tkinter import *

expression = ""

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = expresssion.get()
	return userInput


# this is the function called when the button is clicked
def t():
	print('clicked')


# this is the function called when the button is clicked
def f():
	print('clicked')


def press(num):
	global expression
	expression += str(num)
	equation.set(expression)


def setLabel():
	text = expresssion.get()
	labelOne["text"] = text
	root.title(text)
	expresssion.delete(0, len(text))






root = Tk()
equation = StringVar()
# This is the section of code which creates the main window
root.geometry('840x520')
root.configure(background='#F0F8FF')
root.title('Calc')


# This is the section of code which creates a text input box
expresssion=Entry(root, textvariable=equation)
expresssion.place(x=356, y=64)


# This is the section of code which creates a button
Button(root, text='1', bg='#F0F8FF', font=('arial', 36, 'normal'), command=lambda: press(1)).place(x=76, y=144)


# This is the section of code which creates a button
Button(root, text='2', bg='#F0F8FF', font=('arial', 36, 'normal'), command=lambda: press(2)).place(x=186, y=144)


# This is the section of code which creates the a label
labelOne = Label(root, text='this is a labelsad', bg='#F0F8FF', font=('arial', 36, 'normal'))
labelOne.place(x=76, y=284)

Button(root, text='Update', bg='#F0F8FF', font=('arial', 36, 'normal'), command=setLabel).place(x=280, y=144)



root.mainloop()
