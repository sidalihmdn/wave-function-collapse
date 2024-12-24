from consts import *

rules = {
    BLANK: {
        "UP": [UP, BLANK,],
        "DOWN": [DOWN, BLANK],
        "LEFT": [LEFT, BLANK],
        "RIGHT": [RIGHT, BLANK],
    },
    UP: {
        "UP": [DOWN, RIGHT, LEFT],
        "DOWN": [BLANK, DOWN],
        "LEFT": [RIGHT, DOWN, UP],
        "RIGHT": [LEFT, DOWN, UP],
    },
    DOWN: {
        "UP": [BLANK, UP],
        "DOWN": [UP, LEFT, RIGHT],
        "LEFT": [RIGHT, UP, DOWN],
        "RIGHT": [LEFT, UP, DOWN],
    },
    LEFT: {
        "UP": [RIGHT, DOWN, LEFT],
        "DOWN": [LEFT, UP, RIGHT],
        "LEFT": [DOWN, RIGHT, UP],
        "RIGHT": [BLANK, RIGHT, LEFT],
    },
    RIGHT: {
        "UP": [LEFT, DOWN, RIGHT],
        "DOWN": [RIGHT, UP, LEFT],
        "LEFT": [BLANK, LEFT],
        "RIGHT": [DOWN, LEFT, UP],
    }
}

print(rules[UP]["UP"]) # [DOWN, RIGHT, LEFT]