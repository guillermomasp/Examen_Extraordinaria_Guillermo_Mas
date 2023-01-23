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

