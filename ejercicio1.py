import tkinter as tk

class DotsAndBoxes(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dots and Boxes")
        self.geometry("300x300")

        self.canvas = tk.Canvas(self, width=250, height=250)
        self.canvas.pack()

        self.create_grid()
        self.bind_events()

    def create_grid(self):
        for i in range(5):
            self.canvas.create_line(50 * i, 0, 50 * i, 250)
            self.canvas.create_line(0, 50 * i, 250, 50 * i)

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.draw_line)



