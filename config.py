WIN_WIDTH = 640     #window width
WIN_HEIGHT = 480    #window height
TILE_SIZE = 32         #size of tiles (in pixels)
FPS = 60
PLAYER_LAYER = 2    #layer of player (above ground)
BLOCK_LAYER = 1     #layer of blocks
BLACK = (0, 0, 0)
RED = (255, 0, 0)   #color red (rgb tuple)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
GOLD = (206, 184, 136)
GARNET = (120, 47, 64)

DIALOG_BOX_WIDTH = WIN_WIDTH - WIN_WIDTH//3
DIALOG_BOX_HEIGHT = int((1/4)*WIN_HEIGHT)
DIALOG_BOX_X = int((1/6)*WIN_WIDTH)
DIALOG_BOX_Y = DIALOG_BOX_HEIGHT*3-int((1/6)*DIALOG_BOX_HEIGHT)
DIALOG_BOX_MARGIN = 5

player_image = "images/player_stand.png"
nurse_image = "images/nurse_front.png"
trainer_image = "images/trainer_front.png"

tilemap = [
    'BBBBBBBBBXXBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B....T.............B',
    'X..................X',
    'X.........P........X',
    'X..................X',
    'B..................B',
    'B..................B',
    'B..................B',
    'B...............N..B',
    'B..................B',
    'BBBBBBBBBXXBBBBBBBBB'
]

tilemap2 = [
    'BBBBBBBBBXXBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'X..................X',
    'X..................X',
    'X..................X',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B.........P........B',
    'BBBBBBBBBXXBBBBBBBBB'
]