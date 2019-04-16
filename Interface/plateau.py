from tkinter import *
import random

class Plateau():

    def __colorGet(self):
        colorList = [
            "#a12b0d",
            "#852006",
            "#d28639",
            "#b819f0",
            "#f0cb2f",
            "#f9f6c9",
            "#ffccff",
            "#eecad0",
            "#999966",
            "#666666",
            "#cccccc",
            "#cbb3d0",
            "#8d1a93",
            "#afec57",
            "#feffd1",
            "#642d44"
        ]
        return colorList

    def getRandowColor(self):
        lengthLIst = self.__colorGet().__len__()
        numRandom = random.randint(0, lengthLIst)
        return self.__colorGet()[(numRandom - 1)]

    def drawGrid(self):
        # i & j = grid size || i = vertical size || j = horizontal size
        for i in range(15):
            for j in range(35):
                rectangle = Frame(self.root, highlightbackground=self.getRandowColor(), width=40, height=40, highlightthickness=3)
                b = rectangle
                b.grid(row=i, column=j, sticky="ns")

    def get_root(self):
        return self.root

    def __init__(self):
        self.root = Tk()

        self.root.title("Square Game")

        self.drawGrid()

        self.root.mainloop()



