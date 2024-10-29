from tkinter import *

root = Tk()

#btn = Button(root, text='Click me!')
#btn.pack()
my_label = Label(root, text='Hello World!')
my_label_2 = Label(root, text='My name is Yuri')

#my_label.grid(row=0, column=0)
#my_label_2.grid(row=2, column=1)

def click_handler():
    entry_text = entry_field.get()
    my_label = Label(text=f'{entry_text} - your input')
    my_label.pack()

entry_field = Entry(root)
entry_field.pack()

btn = Button(root, text='Click me!', padx='100', pady='50', bg='purple', fg='white', bd='5', command=click_handler)

btn.pack()
#my_label_2.pack()
#my_label.pack()

root.mainloop()