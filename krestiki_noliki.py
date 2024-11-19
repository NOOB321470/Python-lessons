from tkinter import *
#TODO change import method, to from tkinter import module
# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO= CANVAS_SIZE//FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

# players setup
X = 'player 1'
O = 'player 2'
FIRST_PLAYER= X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    def build_grid(self, grid_color):
        x = CANVAS_SIZE//RATIO
        y1 = 0
        y2 = CANVAS_SIZE
        for _ in range(2):
            self.canvas.create_line(x, y1, x, y2, fill = grid_color)
            self.canvas.create_line(y1, x, y2, x, fill=grid_color)
            x+= CANVAS_SIZE//RATIO
    def render_cross(self, posX, posY):
        pass
    def render_circle(self, posX, posY):
        pass
    def winner(self, player=None):
        pass
#создадим объект класса Board и проверим работоспособность программы
game_v1 = Board(start_player=FIRST_PLAYER)

#запускаем игру
game_v1.mainloop()