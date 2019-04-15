from tkinter import Canvas, Tk, BOTH

class Plateau():

    def DrawGrid(self, event=None):
        # Get current width of canvas
        w = self._set_canvas.winfo_width()
        # Get current height of canvas
        h = self._set_canvas.winfo_height()
        # Will only remove the grid_line
        self._set_canvas.delete('grid_line')

        # Creates all vertical lines at intevals of 100
        for i in range(0, w, 100):
            self._set_canvas.create_line([(i, 0), (i, h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, h, 100):
            self._set_canvas.create_line([(0, i), (w, i)], tag='grid_line')

        print("Coucou")

    def get_root(self):
        return self.root

    def __init__(self):
        self. root = Tk()
        self._set_canvas = Canvas(self.root, height=1000, width=1000, bg='white')
        self._set_canvas.pack(fill=BOTH, expand=True)
        self._set_canvas.bind('<Configure>', self.DrawGrid)
        self.root.mainloop()



