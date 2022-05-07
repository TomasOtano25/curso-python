import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, root=None):
        self.root = root
        self.pack()
        self.config(width=480, height=320, bg='green')
