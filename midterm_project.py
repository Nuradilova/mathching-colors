import tkinter as tk
from random import shuffle
import numpy as np
#from tkinter import messagebox

COLORS = ['red', 'yellow', 'blue', 'purple', 'green', 'brown', 'black', 'orange', 'pink', 'grey', 'maroon', 'silver', 'gold']

class Block:
    def __init__(self, value):
        self.value = value
        self.visible = False
        self.color = COLORS[value]
        self.is_dead = False


class Universe:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.number_of_elements = row * column
        self.matrix = []

        canvas = tk.Canvas(root, width=720, height=720)
        canvas.bind('<Button-1>', self.open_color)

        canvas.pack()

        self.c = canvas

        self.block_height = 720 / row
        self.block_width = 720 / column

        if self.number_of_elements % 2 == 1:
            raise Exception('The number of cells can not be odd')

        for i in range(self.number_of_elements // 2):
            self.matrix.append(Block(i))
            self.matrix.append(Block(i))

        shuffle(self.matrix)

        self.matrix = np.array(self.matrix)
        self.matrix = self.matrix.reshape((row, column)).tolist()

        self.is_open = False
        self.last_opened = None

    def console(self):
        for row in self.matrix:
            for el in row:
                print(el.value, end=' ')
            print()

    def console_color(self):
        for row in self.matrix:
            for el in row:
                print(el.color, end=' ')
            print()

    def display(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.matrix[i][j].visible:
                    color = self.matrix[i][j].color
                else:
                    color = '#ebebeb'

                self.c.create_rectangle(
                    j * self.block_width,
                    i * self.block_height,
                    (j+1) * self.block_width,
                    (i+1) * self.block_height,
                    fill=color
                )

    def open_color(self, event):
        i = int(event.y // self.block_height)
        j = int(event.x // self.block_width)

        if self.matrix[i][j].is_dead:
            return
        # self.matrix[i][j].visible = not self.matrix[i][j].visible


        if not self.is_open:
            self.last_opened = self.matrix[i][j]
            self.matrix[i][j].visible = True
            self.is_open = True
        else:
            print(self.last_opened.value, self.matrix[i][j].value)
            if self.last_opened.value == self.matrix[i][j].value:
                self.last_opened.is_dead = True
                self.matrix[i][j].is_dead = True
                self.matrix[i][j].visible = True
                self.last_opened.visible = True

            else:
                self.last_opened.visible = False

            self.is_open = False

        self.display()

root = tk.Tk()
root.geometry('720x720')
root.resizable(False, False)



u = Universe(4, 4)
u.console()
u.console_color()
u.display()

root.mainloop()