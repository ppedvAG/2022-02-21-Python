from tkinter import *
from tkinter import ttk
root = Tk()
root.title("New Calc")
root.geometry("250x150")

expressionField = ttk.Entry(root)

expressionField.grid(columnspan=5, ipadx=50, pady=15)
button1 = ttk.Button(root, text="1")
button2 = ttk.Button(root, text="2")
button3 = ttk.Button(root, text="3")
button4 = Button(root, text="4")

button1.grid(row=2, column=0, padx=10)
button2.grid(row=2, column=1, padx=10)
button3.grid(row=2, column=2, padx=10)
button4.grid(row=3, column=0, padx=10)

root.mainloop()
