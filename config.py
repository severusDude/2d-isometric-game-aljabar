SPRITE_CHARACTER_FILE = R"img/character.png"
SPRITE_TERRAIN_FILE = R"img/terrain.png"

SPRITE_BLOCK_COORD = (960, 448)
SPRITE_TERRAIN_COORD = (64, 352)

SPRITE_CHARACTER = {
    'down': [(3, 2), (35, 2), (68, 2)],
    'up': [(3, 34), (35, 34), (68, 34)],
    'left': [(3, 98), (35, 98), (68, 98)],
    'right': [(3, 66), (35, 66), (68, 66)]
}


WIN_WIDTH = 640
WIN_HEIGHT = 480
TILE_SIZE = 32
FPS = 60

PLAYER_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1
PLAYER_SPEED = 3

COLOR_RED = (255, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)

tilemap = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B..................B",
    "B..................B",
    "B...BBB............B",
    "B..................B",
    "B..................B",
    "B.......P..........B",
    "B..................B",
    "B.....BB...........B",
    "B......B...........B",
    "B......B...........B",
    "B......B...........B",
    "B..................B",
    "B..................B",
    "BBBBBBBBBBBBBBBBBBBB",
]
