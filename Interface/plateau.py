from tkinter import Tk, Canvas, Frame, BOTH

class Plateau(Frame):

    def DrawGrid(self):

        # draw horizontal lines
        x1 = 0
        x2 = 450
        for k in range(0, 500, 50):
            y1 = k
            y2 = k
            Canvas.create_line(x1, y1, x2, y2)
        # draw vertical lines
        y1 = 0
        y2 = 450
        for k in range(0, 500, 50):
            x1 = k
            x2 = k
            Canvas.create_line(x1, y1, x2, y2)

    def __init__(self):
        super().__init__()
        self.DrawGrid()



