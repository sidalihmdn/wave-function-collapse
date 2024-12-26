import pygame
import os
from grid import Grid, Tile
from consts import *

def load_tiles():
    # load all the file from /tiles that start with "tile"
    images= {}
    connections = {}
    images[UP] = pygame.image.load(os.path.join("tiles", "tile_up.png"))
    connections[UP] = [1,1,1,0]
    images[DOWN] = pygame.image.load(os.path.join("tiles", "tile_down.png"))
    connections[DOWN] = [1,0,1,1]
    images[LEFT] = pygame.image.load(os.path.join("tiles", "tile_left.png"))
    connections[LEFT] = [1,1,0,1]
    images[RIGHT] = pygame.image.load(os.path.join("tiles", "tile_right.png"))
    connections[RIGHT] = [0,1,1,1]
    images[BLANK] = pygame.image.load(os.path.join("tiles", "tile_blank.png"))
    connections[BLANK] = [0,0,0,0]

    # return a list of all the tiles
    return images , connections



if __name__ == "__main__":
    images, connections = load_tiles()
    tiles = {}
    for key in images.keys():
        print("connections", connections[key])
        tiles[key] = Tile(images[key], connections[key])

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Collapse")
    window = pygame.display.set_mode((CELL_SIZE*GRID_SIZE, CELL_SIZE*GRID_SIZE))
    grid = Grid(GRID_SIZE, tiles)
    grid.fill()
    grid[3,3].set_tile(tiles[UP])
    grid.calculate_options()


    while True:
        for event in pygame.event.get():
            grid.draw(window)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid.collapse()

        pygame.display.flip()