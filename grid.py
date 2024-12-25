import pygame
import random
from consts import *



class Grid:
    def __init__(self, cell_number, tiles):
        self.cell_number = cell_number
        self.hight = cell_number * CELL_SIZE
        self.width = cell_number * CELL_SIZE
        self.cells = []
        self.tiles = tiles

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

    def calculate_options(self):
        for i in range(self.cell_number):
            for j in range(self.cell_number):
                cell = self.cells[i][j]
                if cell.is_collapse:
                    continue
                available_options = [tile.connection for tile in self.tiles.values()]
                neighbor_1 = self.cells[i][j+1] if j+1 < self.cell_number else None
                neighbor_2 = self.cells[i+1][j] if i+1 < self.cell_number else None
                neighbor_3 = self.cells[i][j-1] if j-1 >= 0 else None
                neighbor_4 = self.cells[i-1][j] if i-1 >= 0 else None

                if neighbor_1 and neighbor_1.tile:
                    neighbor_1_rules = neighbor_1.tile.adjacency_rules(self.tiles)[LEFT]
                    available_options = intersect(available_options, neighbor_1_rules)

                if neighbor_2 and neighbor_2.tile:
                    neighbor_2_rules = neighbor_2.tile.adjacency_rules(self.tiles)[UP]
                    available_options = intersect(available_options, neighbor_2_rules)

                if neighbor_3 and neighbor_3.tile:
                    neighbor_3_rules = neighbor_3.tile.adjacency_rules(self.tiles)[RIGHT]
                    available_options = intersect(available_options, neighbor_3_rules)

                if neighbor_4 and neighbor_4.tile:
                    neighbor_4_rules = neighbor_4.tile.adjacency_rules(self.tiles)[DOWN]
                    available_options = intersect(available_options, neighbor_4_rules)

    
def intersect(list_a, list_b):
    set_a = {tuple(a) for a in list_a}
    set_b = {tuple(b) for b in list_b}

    return [list(a) for a in set_a & set_b]


class Cell:
    def __init__(self, x, y):
        self.is_collapse = False
        self.options = [UP, DOWN, LEFT, RIGHT]
        self.x = x
        self.y = y
        self.value = -1
        self.options = []
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
    
    def adjacency_rules(self , tiles):
        rules = {
            UP: [],
            DOWN: [],
            LEFT: [],
            RIGHT: []
        }
        for tile in tiles.values():
            if self.connection[0] == tile.connection[-2]:
                rules[LEFT].append(tile.connection)
            if self.connection[1] == tile.connection[-1]:
                rules[UP].append(tile.connection)
            if self.connection[2] == tile.connection[0]:
                rules[RIGHT].append(tile.connection)
            if self.connection[3] == tile.connection[1]:
                rules[DOWN].append(tile.connection)
        return rules

