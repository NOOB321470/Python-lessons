from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

canvas.create_rectangle(10, 10, 10, 10, fill='red')

canvas.create_rectangle(70, 70, 450, 450)
canvas.create_line(20, 20, 400, 20)
canvas.create_line(20, 20, 20, 400)
canvas.create_line(20, 20, 70, 70)
canvas.create_line(400, 20, 450, 70)
canvas.create_line(20, 400, 70, 450)

canvas.create_oval(200, 200, 400, 400)

canvas.create_polygon(40, 20, 100, 50, 100, 110, fill='blue')

canvas.create_text(200, 200, text='Hello world', fill='red', activefill='green', font='Arial 40')
root.mainloop()