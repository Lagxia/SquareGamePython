import Interface.plateau

from tkinter import Tk, Canvas, Frame, BOTH

def main():
    root = Tk()
    canvas = Tk.Canvas(root, width=450, height=450, bg='white')
    canvas.pack()
    ex = Interface.plateau.Plateau()
    root.mainloop()

if __name__ == '__main__':
    main()