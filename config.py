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
    'BT.......T........TB',
    'BT......T.T.......TB',
    'BT.....T...T......TB',
    'BT....T.....T.....TB',
    'BT...T.......T....TB',
    'BT..T.........T...TB',
    'BTTTTTTTTPTTTTTTTTNB',
    'BT..T.........T...TB',
    'BT...T.......T....TB',
    'BT....T.....T.....TB',
    'BT.....T...T......TB',
    'BT......T.T.......TB',
    'BT.......T........TB',
    'BBBBBBBB11111BBBBBBB'
]
,
#tilemap[1]
[   'BBBBBBBBBBBBBBBBBBBB',
    'BT.......T........TB',
    'BT......T.T.......TB',
    'BT.....T...T......TB',
    'BT....T.....T.....TB',
    'BT...T.......T....TB',
    'BT..T.........T...TB',
    'BTTTTTTTTTTTTTTTTTNB',
    'BT..T.........T...TB',
    'BT...T.......T....TB',
    'BT....T.....T.....TB',
    'BT.....T...T......TB',
    'BT......T.T.......TB',
    'BT.......P........TB',
    'BBBBBBBB11111BBBBBBB'
]
]


#Path near HCB (935, 646)
tilemap1 = [[                   
    'BBBBBBBBXXXXXBBBBBBB',
    'B......BTTPTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTBBBBBBB',
    'B......DTTTTTTTTTTT4',
    'B.......TTTTTTTTTTT4',
    'B.......TTTTTTTTTTT4',
    'B......BTTTTTBBBBBBB',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'BBBBBBBB22222BBBBBBB'
]
,
#tilemap1[1]
[   
    'BBBBBBBBXXXXXBBBBBBB',
    'B......BTTPTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTBBBBBBB',
    'B......DTTTTTTTTTTT4',
    'B.......TTTTTTTTTTP4',
    'B.......TTTTTTTTTTT4',
    'B......BTTTTTBBBBBBB',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'BBBBBBBB22222BBBBBBB'
]
,
#tilemap1[2]
[
    'BBBBBBBBXXXXXBBBBBBB',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTBBBBBBB',
    'B......DTTTTTTTTTTT4',
    'B.......TTTTTTTTTTT4',
    'B.......TTTTTTTTTTT4',
    'B......BTTTTTBBBBBBB',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTPTTB.....B',
    'BBBBBBBB22222BBBBBBB'
]
,
#tilemap1[3]
[
    'BBBBBBBBXXXXXBBBBBBB',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTBBBBBBB',
    'B......DTTTTTTTTTTT4',
    'B.......TTTTTTTTTTP4',
    'B.......TTTTTTTTTTT4',
    'B......BTTTTTBBBBBBB',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'B......BTTTTTB.....B',
    'BBBBBBBB22222BBBBBBB'
]
]

#area outside union
tilemap2=[[
    'BBBBBBBB11111BBBBBBB',
    'B.......TTPTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    '3TTTTTTTTTTTT......B',
    '3TTTTTTTTTTTT......B',
    'BBBBBBBBBBBBBBBBBBBB'
]
,
#tilemap2[1]
[
    'BBBBBBBB11111BBBBBBB',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    'B.......TTTTT......B',
    '3PTTTTTTTTTTT......B',
    '3TTTTTTTTTTTT......B',
    'BBBBBBBBBBBBBBBBBBBB'
]
]

#union
tilemap3 = [
    'BBBBBBBBBBBBBBBBBBBB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFNFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFP2',
    'BFFFFFFFFFFFFFFFFFF2',
    'BBBBBBBBBBBBBBBBBBBB'
]

#statue area
tilemap4 = [
[
    'BBBBBBBB555555BBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B......TTTTTTTT....B',
    'B.....TTBBBBBBTT...B',
    '1TTTTTTBTTTTTTBTTTT7',
    '1PTTTTTBTTTTTTBTTTT7',
    '1TTTTTTBTTTTTTBTTTT7',
    'B.....TTBBBBBBTT...B',
    'B......TTTTTTTT....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBBBBBBBBBBBBB'
]
,
#tilemeap4[1]
[
    'BBBBBBBB555555BBBBBB',
    'B.......TTPTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B......TTTTTTTT....B',
    'B.....TTBBBBBBTT...B',
    '1TTTTTTBTTTTTTBTTTT7',
    '1TTTTTTBTTTTTTBTTTT7',
    '1TTTTTTBTTTTTTBTTTT7',
    'B.....TTBBBBBBTT...B',
    'B......TTTTTTTT....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBBBBBBBBBBBBB'
]
,
#tilemap4[2]
[
    'BBBBBBBB555555BBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B......TTTTTTTT....B',
    'B.....TTBBBBBBTT...B',
    '1TTTTTTBTTTTTTBTTTT7',
    '1TTTTTTBTTTTTTBTTTP7',
    '1TTTTTTBTTTTTTBTTTT7',
    'B.....TTBBBBBBTT...B',
    'B......TTTTTTTT....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBBBBBBBBBBBBB'
]
]

#path to HWC and entrance to leach
tilemap5= [
[
    'BBBBBBBBBBBBBBBBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTPTTT.....B',
    'BBBBBBBB444444BBBBBB'        
]
,
#tilemap5[1]
[
    'BBBBBBBBBBBBBBBBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTTTTTTP6',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBB444444BBBBBB' 
]
]

#HWC
tilemap6= [
    'BBBBBBBBBBBBBBBBBBBB',
    'BFFFFFFFFFFFFFFFFFFB',
    '5FFFFFFFFFFFFFFFFFFB',
    '5PFFFFFFFFFFFFFFFFFB',
    '5FFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFNFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BBBBBBBBBBBBBBBBBBBB'
]

#between statue and dirac 4 route 
tilemap7= [[
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
    '4TTTTTTTTTTTTTTTTTT8',
    '4PTTTTTTTTTTTTTTTTT8',
    '4TTTTTTTTTTTTTTTTTT8',
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]
,
#tilemap7[1]
[
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
    '4TTTTTTTTTTTTTTTTTT8',
    '4TTTTTTTTTTTTTTTTTP8',
    '4TTTTTTTTTTTTTTTTTT8',
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]
]

#path near dirac
tilemap8 = [
[
    'BBBBBBBB++++++BBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBTTTTTTBBBBBB',
    '7TTTTTTTTTTTTTTTTTT8',
    '7PTTTTTTTTTTTTTTTTT8',
    '7TTTTTTTTTTTTTTTTTT8',
    'BBBBBBBBTTTTTTBBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBB999999BBBBBB'
]
,
#tilemap8[1]
[
    'BBBBBBBB++++++BBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBTTTTTTBBBBBB',
    '7TTTTTTTTTTTTTTTTTTB',
    '7TTTTTTTTTTTTTTTTTTB',
    '7TTTTTTTTTTTTTTTTTTB',
    'BBBBBBBBTTTTTTBBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTPTTT.....B',
    'BBBBBBBB999999BBBBBB'
]
,
#tilemap8[2]
[
    'BBBBBBBB++++++BBBBBB',
    'B.......TTPTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBTTTTTTBBBBBB',
    '7TTTTTTTTTTTTTTTTTTB',
    '7TTTTTTTTTTTTTTTTTTB',
    '7TTTTTTTTTTTTTTTTTTB',
    'BBBBBBBBTTTTTTBBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBB999999BBBBBB'
]
]

#path into dirac
tilemap9= [
[
    'BBBBBBBB888888BBBBBB',
    'B.......TTPTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]   
,
#tilemap9[1]
[
    'BBBBBBBB888888BBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    '*PTTTTTTTTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]
]

#Dirac
tilemap10 = [
    'BBBBBBBBBBBBBBBBBBBB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTT9',
    'BTTTTTTTTTNTTTTTTTP9',
    'BTTTTTTTTTTTTTTTTTT9',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BTTTTTTTTTTTTTTTTTTB',
    'BBBBBBBBBBBBBBBBBBBB'
]

#path to leach
tilemap11= [
[
    'BBBBBBBB======BBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTPTTT.....B',
    'BBBBBBBB888888BBBBBB'
]
,
#tilemap11[1]
[
    'BBBBBBBB======BBBBBB',
    'B.......TTPTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBB888888BBBBBB'
]
]

#entrance to leach (-)
tilemap12= [
[
    'BBBBBBBBBBBBBBBBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTPTTT.....B',
    'BBBBBBBB++++++BBBBBB'  
]
,
#tilemap12[1]
[
    'BBBBBBBBBBBBBBBBBBBB',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTTTTTTP-',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBB++++++BBBBBB' 
]
]

#leach
tilemap13= [
    'BBBBBBBBBBBBBBBBBBBB',
    'BFFFFFFFFFFFFFFFFFFB',
    '=FFFFFFFFFFFFFFFFFFB',
    '=PFFFFFFFFFFFFFFFFFB',
    '=FFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BFFFFFFFFFFFFFFFFFFB',
    'BBBBBBBBBBBBBBBBBBBB'
]
