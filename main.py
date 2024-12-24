import pygame
import os
from grid import Grid, Tile
from consts import *

def load_tiles():
    # load all the file from /tiles that start with "tile"
    tiles = {}
    connections = {}
    tiles[UP] = pygame.image.load(os.path.join("tiles", "tile_up.png"))
    connections[UP] = [1,1,1,0]
    tiles[DOWN] = pygame.image.load(os.path.join("tiles", "tile_down.png"))
    connections[DOWN] = [1,0,1,1]
    tiles[LEFT] = pygame.image.load(os.path.join("tiles", "tile_left.png"))
    connections[LEFT] = [1,1,0,1]
    tiles[RIGHT] = pygame.image.load(os.path.join("tiles", "tile_right.png"))
    connections[RIGHT] = [0,1,1,1]
    tiles[BLANK] = pygame.image.load(os.path.join("tiles", "tile_blank.png"))
    connections[BLANK] = [0,0,0,0]

    # return a list of all the tiles
    return tiles , connections

def adjacency_rules(tile , connections):
    rules = {
        UP: [],
        DOWN: [],
        LEFT: [],
        RIGHT: []
    }
    for connection in connections.values():
        if tile[0] == connection[-2]:
            rules[LEFT].append(connection)
        if tile[1] == connection[-1]:
            rules[UP].append(connection)
        if tile[2] == connection[0]:
            rules[RIGHT].append(connection)
        if tile[3] == connection[1]:
            rules[DOWN].append(connection)
    return rules



if __name__ == "__main__":
    tiles, connections = load_tiles()

    rules = adjacency_rules(connections[0] , connections)
    print(rules)
    pygame.init()
    pygame.display.set_caption("Collapse")
    window = pygame.display.set_mode((800,800))
    grid = Grid(GRID_SIZE)
    grid.fill()
    grid[3,3].set_tile(Tile(tiles[UP], connections[UP]))
    grid[3,3].set_value(DOWN)
    grid.draw(window)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            pygame.display.flip()