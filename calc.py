from tkinter import *

root = Tk()

root.title('Simple Calculator 2024')

entry_field = Entry(root, width=40, borderwidth=5)

entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button1 = Button(root, text='1', padx=40, pady=20)
button2 = Button(root, text='2', padx=40, pady=20)
button3 = Button(root, text='3', padx=40, pady=20)
button4 = Button(root, text='4', padx=40, pady=20)
button5 = Button(root, text='5', padx=40, pady=20)
button6 = Button(root, text='6', padx=40, pady=20)
button7 = Button(root, text='7', padx=40, pady=20)
button8 = Button(root, text='8', padx=40, pady=20)
button9 = Button(root, text='9', padx=40, pady=20)
button0 = Button(root, text='0', padx=40, pady=20)
button_add = Button(root, text='+', padx = 39, pady = 20)
button_equal = Button(root, text='=', padx = 40, pady= 20)
button_clear = Button(root, text='Clear', padx = 40, pady = 20)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_add.grid(row=5, column=0)

button_clear.grid(row=4, column=1, columnspan=2, sticky='we')
button_equal.grid(row=5, column=1, columnspan=2, sticky='we')

root.mainloop()