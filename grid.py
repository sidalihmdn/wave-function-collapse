import pygame

CELL_SIZE = 100
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

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
        return self.cells[y/CELL_SIZE][x/CELL_SIZE]

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
        self.tile : pygame.image = None
    
    def collapse(self):
        self.is_collapse = True

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, CELL_SIZE, CELL_SIZE))