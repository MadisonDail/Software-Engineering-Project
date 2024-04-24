WIN_WIDTH = 640     #window width
WIN_HEIGHT = 480    #window height
TILE_SIZE = 32         #size of tiles (in pixels)
FPS = 60
PLAYER_LAYER = 3    #layer of player (above ground)
DIALOG_LAYER = 4    #layer of 
BLOCK_LAYER = 2    #layer of blocks
GROUND_LAYER = 1
BLACK = (0, 0, 0)
RED = (255, 0, 0)   #color red (rgb tuple)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
GOLD = (206, 184, 136)
GARNET = (120, 47, 64)
DEFAULT_SPEED = 5
SELECTGOLD = (206, 124, 136)

DIALOG_BOX_WIDTH = WIN_WIDTH - WIN_WIDTH//3
DIALOG_BOX_HEIGHT = int((1/4)*WIN_HEIGHT)
DIALOG_BOX_X = int((1/6)*WIN_WIDTH)
DIALOG_BOX_Y = DIALOG_BOX_HEIGHT*3-int((1/6)*DIALOG_BOX_HEIGHT)
DIALOG_BOX_MARGIN = 5

DIALOG_OPTION_WIDTH = int((1/3)*DIALOG_BOX_WIDTH)
DIALOG_OPTION_HEIGHT = int((1/3)*DIALOG_BOX_HEIGHT)
DIALOG_OPTION_X = DIALOG_BOX_X+DIALOG_BOX_WIDTH-DIALOG_OPTION_WIDTH
DIALOG_OPTION_Y = DIALOG_BOX_Y-DIALOG_OPTION_HEIGHT-DIALOG_BOX_MARGIN

player_image = "images/ash.png"
nurse_image = "images/player_stand.png"
trainer_image = "images/player_stand.png"

#Map Layouts
tilemap_template=[
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]

#spawn/landis (64, 352)
tilemap = [[         
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B....D.............B',
    'B..................B',
    'B..................B',
    'B.........P........B',
    'B..................B',
    'B............N.....B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBB11BBBBBBBBB'
]
,
#tilemap[1]
[   'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B....D.............B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B............N.....B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B.........P........B',
    'BBBBBBBBB11BBBBBBBBB'
]
]


#Path near HCB (935, 646)
tilemap1 = [[                   
    'BBBBBBBBBXXBBBBBBBBB',
    'B......B..P..B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....BBBBBBB',
    'B......B...........X',
    'B..................X',
    'B......B...........X',
    'B......B.....BBBBBBB',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'BBBBBBBBB22BBBBBBBBB'
]
,
#tilemap1[1]
[   
    'BBBBBBBBBXXBBBBBBBBB',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....BBBBBBB',
    'B......B...........X',
    'B.................PX',
    'B......B...........X',
    'B......B.....BBBBBBB',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'BBBBBBBBB22BBBBBBBBB'
]
,
#tilemap1[2]
[
    'BBBBBBBBBXXBBBBBBBBB',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....BBBBBBB',
    'B......B...........X',
    'B..................X',
    'B......B...........X',
    'B......B.....BBBBBBB',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B.....B.....B',
    'B......B..P..B.....B',
    'BBBBBBBBB22BBBBBBBBB'
]
]

tilemap2=[
    'BBBBBBBBB11BBBBBBBBB',
    'B.........P........B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]