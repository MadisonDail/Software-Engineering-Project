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
    'WWWWWWWWWWWWWWWWWWWW',
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
    'BT...RT.....T.....TB',
    'BT...T.......T....TB',
    'BT..T.........T...TB',
    'BTTTTTTTTTTTTTTTTTNB',
    'BT..T.........T...TB',
    'BT...T.......T....TB',
    'BT....T.....T.....TB',
    'BT.....T...Tl.....TB',
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
    'B......TTTTTTTTTTTT4',
    'B......TTTTTTTTUTTT4',
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
    'B......TTTTTTTTTTTP4',
    'B......TTTTTTTTUTTT4',
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
    'B......TTTTTTTTTTTT4',
    'B......TTTTTTTTTTTT4',
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
    'B......TTTTTTTTTTTP4',
    'B......TTTTTTTTTTTT4',
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
    'W.......TTPTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    '3TTTTTTTTTTTT......B',
    '3TTTTTTTTUTTT......B',
    'WBBBBBBBBBBBBBBBBBBB'
]
,
#tilemap2[1]
[
    'BBBBBBBB11111BBBBBBB',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    'W.......TTTTT......B',
    '3PTTTTTTTTTTT......B',
    '3TTTTTTTTUTTT......B',
    'WBBBBBBBBBBBBBBBBBBB'
]
]

#union
tilemap3 = [
    'WWWWWWWWWWWWWWWWWWWW',
    'WFRFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFNFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFP2',
    'WFFFFFFFFFFFFFFFFFF2',
    'WWWWWWWWWWWWWWWWWWWW'
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
    '1TTTTTTB....Z.BTTTT7',
    '1PTTTTTB.A....BTTTT7',
    '1TTTTTTB..M...BTTTT7',
    'B.....TTBBBBBBTT...B',
    'B......TTTTTTTT....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBSSSSSSBBBBBB'
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
    '1TTTTTTB.M..A.BTTTT7',
    '1TTTTTTB......BTTTT7',
    '1TTTTTTB..Z...BTTTT7',
    'B.....TTBBBBBBTT...B',
    'B......TTTTTTTT....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBSSSSSSBBBBBB'
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
    '1TTTTTTB....M.BTTTT7',
    '1TTTTTTB...Z..BTTTP7',
    '1TTTTTTB.A....BTTTT7',
    'B.....TTBBBBBBTT...B',
    'B......TTTTTTTT....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'B.......TTTTTT.....B',
    'BBBBBBBBSSSSSSBBBBBB'
]
]

#path to HWC
tilemap5= [
[
    'BBBBBBBBSSSSSSBBBBBW',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTPTTT.....W',
    'BBBBBBBB444444BBBBBB'        
]
,
#tilemap5[1]
[
    'BBBBBBBBSSSSSSBBBBBW',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTTTTTTP6',
    'B.......TTTTTTTTTTT6',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'BBBBBBBB444444BBBBBB' 
]
]

#HWC
tilemap6= [
    'WWWWWWWWWWWWWWWWWWWW',
    'WFFFFFFFFFFFFFFFFFFW',
    '5FFFFFFFFFFFFFFFFFFW',
    '5PFFFFFFFFFFFFFFFDFW',
    '5FFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFNFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFRFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WWWWWWWWWWWWWWWWWWWW'
]

#between statue and dirac 4 route 
tilemap7= [[
    'BBBBBBBBhhhBBBBBBBBB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BBBBBBBBBBBBBBBBBBBB',
    '4TTTTTTTTTTTTTTTTTT8',
    '4PTTTTTTTTTTTTTTTTT8',
    '4TTTTTTTTTTTTTTTTTT8',
    'BBBBBBBBBBBBBBBBBBBB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BBBBBBBBBBBBBBBBBBBB'
]
,
#tilemap7[1]
[
    'BBBBBBBBhhhBBBBBBBBB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BBBBBBBBBBBBBBBBBBBB',
    '4TTTTTTTTTTTTTTTTTT8',
    '4TTTTTTTTTTTTTTTTTP8',
    '4TTTTTTTTTTTTTTTTTT8',
    'BBBBBBBBBBBBBBBBBBBB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BBBBBBBBBBBBBBBBBBBB'
]
,
#tilemap7[2]
[
    'BBBBBBBBhhhBBBBBBBBB',
    'BwwwwwwwwPwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BBBBBBBBBBBBBBBBBBBB',
    '4TTTTTTTTTTTTTTTTTT8',
    '4TTTTTTTTTTTTTTTTTT8',
    '4TTTTTTTTTTTTTTTTTT8',
    'BBBBBBBBBBBBBBBBBBBB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
    'BwwwwwwwwwwwwwwwwwwB',
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
    '7TTTTTTTTTTTTTTTTTTS',
    '7PTTTTTTTTTTTTTTTTTS',
    '7TTTTTTTTTTTTTTTTTTS',
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
    '7TTTTTTTTTTTTTTTTTTS',
    '7TTTTTTTTTTTTTTTTTTS',
    '7TTTTTTTTTTTTTTTTTTS',
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
    '7TTTTTTTTTTTTTTTTTTS',
    '7TTTTTTTTTTTTTTTTTTS',
    '7TTTTTTTTTTTTTTTTTTS',
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
    'W.......TTPTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    'W..................B',
    'W..................B',
    'W..................B',
    'W..................B',
    'WBBBBBBBBBBBBBBBBBBB'
]   
,
#tilemap9[1]
[
    'BBBBBBBB888888BBBBBB',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    'W.......TTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    '*PTTTTTTTTTTTT.....B',
    '*TTTTTTTTTTTTT.....B',
    'W..................B',
    'W..................B',
    'W..................B',
    'W..................B',
    'WBBBBBBBBBBBBBBBBBBB'
]
]

#Dirac
tilemap10 = [
    'WWWWWWWWWWWWWWWWWWWW',
    'WTTTTTTTTTTTTTTTTTTW',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTT#TT#TT#TT#TT#TTT9',
    'WTT#TT#TT#NT#TT#TTP9',
    'WTT#TT#TT#TT#TT#TTT9',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTT#TT#TT#TT#TT#TTTW',
    'WTTTTTTTTTTTTTTTTTTW',
    'WWWWWWWWWWWWWWWWWWWW'
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
    'h.......TTTTTT.....B',
    'h.......TTPTTT.....B',
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
    'h.......TTTTTT.....B',
    'h.......TTTTTT.....B',
    'BBBBBBBB888888BBBBBB'
]
,
#tilemap11[2]
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
    'h.......TTTTTT.....B',
    'hP......TTTTTT.....B',
    'BBBBBBBB888888BBBBBB'
]
]

#entrance to leach 
tilemap12= [
[
    'BBBBBBBBBBBBBBBBBBBW',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTPTTT.....W',
    'BBBBBBBB++++++BBBBBB'  
]
,
#tilemap12[1]
[
    'BBBBBBBBBBBBBBBBBBBW',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTTTTTTP-',
    'B.......TTTTTTTTTTT-',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'B.......TTTTTT.....W',
    'BBBBBBBB++++++BBBBBB' 
]
]

#leach
tilemap13= [
    'WWWWWWWWWWWWWWWWWWWW',
    'WFFFFFFFFFFFFFFFFFFW',
    '=FFFFFFFFFFFFFFFFFFW',
    '=PFFFFFFFFFFFFFFFFFW',
    '=FFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WFFFFFFFFFFFFFFFFFFW',
    'WWWWWWWWWWWWWWWWWWWW'
]

#hidden entrance
tilemap_hide1=[
[
    'BBBBBBBBBBBBBBBBBBBB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLTTTTTTTTTTT+',
    'BLLLLLLLTTTTTTTTTTP+',
    'BBBBBBBB777BBBBBBBBB'
]
,
#tilemap_hide1[1]
[
    'BBBBBBBBBBBBBBBBBBBB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLLLLLLLLLLLLB',
    'BLLLLLLLTTTTTTTTTTTT+',
    'BLLLLLLLTPTTTTTTTTTT+',
    'BBBBBBBB777BBBBBBBBB'
]
]