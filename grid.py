import pygame

from consts import *



class Grid:
    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.hight = cell_number * CELL_SIZE
        self.width = cell_number * CELL_SIZE
        self.cells = []

    def fill(self):
        self.cells = [[Cell(n*CELL_SIZE, m*CELL_SIZE) for n in range(self.cell_number)] for m in range(self.cell_number)]

    def draw(self, win):
        win = pygame.display.set_mode((self.width, self.hight))
        for row in self.cells:
            for cell in row:
                cell.draw(win)
                

    def __getitem__(self, pos):
        x, y = pos
        return self.cells[y][x]

    def __setitem__(self, pos, value):
        x, y = pos
        self.cells[y][x] = value

    def __str__(self):
        return "\n".join("".join(str(cell) for cell in row) for row in self.cells)
    

class Cell:
    def __init__(self, x, y):
        self.is_collapse = False
        self.options = [UP, DOWN, LEFT, RIGHT]
        self.x = x
        self.y = y
        self.value = -1
        self.options = []
        self.tile : pygame.image = None
    
    def collapse(self):
        self.is_collapse = True

    def set_value(self, value):
        self.value = value

    def set_tile(self, tile):
        self.tile = tile
    
    def __str__(self):
        return str({
            "is_collapse": self.is_collapse,
            "options": self.options,
            "value": self.value,
            "tile": self.tile,
            "x": self.x,
            "y": self.y
        })


    def draw(self, win):
        if self.tile is not None:
            # draw the image corresponding to the value of the cell
            tile = pygame.transform.scale(self.tile, (CELL_SIZE, CELL_SIZE))
            win.blit(tile, (self.x, self.y))
        else:
            pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, CELL_SIZE, CELL_SIZE))