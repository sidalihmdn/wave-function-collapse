import pygame
import os
from grid import Grid

GRID_SIZE = 4


def load_tiles():
    # load all the file from /tiles that start with "tile"
    tiles = []
    for file in os.listdir("tiles"):
        if file.startswith("tile"):
            tiles.append(pygame.image.load("tiles/" + file))
    # return a list of all the tiles
    return tiles

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Collapse")
    window = pygame.display.set_mode((800,800))
    grid = Grid(GRID_SIZE)
    grid.fill()
    grid.draw(window)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            pygame.display.flip()