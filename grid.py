import pygame
import random
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

    def chech_options(self):
        # check the options for each cell depending on the value of the cell and the rules
        for row in self.cells:
            for cell in row:
                if not cell.is_collapse:
                    cell.options = rules[cell.value]

                

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
        self.options = {
            "UP": [],
            "DOWN": [],
            "LEFT": [],
            "RIGHT": []
        }
        self.tile : Tile = None
    
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
            image = self.tile.image
            image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
            win.blit(image, (self.x, self.y))
        else:
            pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, CELL_SIZE, CELL_SIZE))


class Tile:
    def __init__(self, image, connection):
        self.image : pygame.image = image
        self.connection = connection
    
    def __str__(self):
        return str({
            "image": self.image,
            "connections": self.connections
        })
    
    def adjacency_rules(self , connections):
        rules = {
            UP: [],
            DOWN: [],
            LEFT: [],
            RIGHT: []
        }
        for connection in connections.values():
            if self.connection[0] == connection[-2]:
                rules[LEFT].append(connection)
            if self.connection[1] == connection[-1]:
                rules[UP].append(connection)
            if self.connection[2] == connection[0]:
                rules[RIGHT].append(connection)
            if self.connection[3] == connection[1]:
                rules[DOWN].append(connection)
        return rules

