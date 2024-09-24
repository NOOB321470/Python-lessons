import turtle 


screen = turtle.getscreen()
t = turtle.Turtle()


# t1 = t.clone()
# t.forward(100)
# t1.left(120)
# t.color('white')
# t.begin_fill()
# #t.circle(90)
# t.end_fill()
# t.forward(100)
# t.left(10)
# t.back(100)
# t.forward(100)
# t.left(10)
# t.back(100)
# for i in range(2):
#     t.right(100)
#     t.forward(100)
#     t.back(100)

# 
# for i in range(20):
#     t.forward(100)
#     t.left(250)
class DrawShape:
    def draw(self, color='red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()

class Rect(DrawShape):
    def __init__(self, size, fill=False):
        self.size = size
        self.sides = 4
        self.angle = 90
        self.fill = fill
rect = Rect(80, fill=True)
rect.draw()
t.goto(0,80)
rect.draw('yellow')
t.goto(0,160)
rect.draw('green')
screen.mainloop()