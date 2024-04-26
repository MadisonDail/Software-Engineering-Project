from entity import *
import pygame
import random  #battle encounters 
import battleTest
import pokedex 
import pokemon
import chooseFighter
import copy

class Player(Entity):                       #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen):
        super().__init__(id,game,layer,x,y,spriteImage,screen)
        self.x_change = 0   #temp variable to be added to coordinated in update
        self.y_change = 0
        self.facing = 'down'
        self.starter = chooseFighter.chooseStarter() # gets first pokemon
        self.playerPokemon = []
        self.playerPokemon.append(self.starter)

    def set_position(self,x,y):
        self.rect.topleft = (x*TILE_SIZE,y*TILE_SIZE) 
    
    def stop_movement(self):                #don't allow player sprite to move 
        self.velocity = 0
    
    def resume_movement(self, vel=DEFAULT_SPEED):
        self.velocity = vel                 #allow player to move again

    def movement(self):                     
    # adjust sprite position if a key is pressed
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            self.x_change -= self.velocity  #velocity is element from entity class (speed of player)
            self.facing = 'left'
        if key_press[pygame.K_RIGHT]:
            self.x_change += self.velocity
            self.facing = 'right'
        if key_press[pygame.K_UP]:
            self.y_change -= self.velocity
            self.facing = 'right'
        if key_press[pygame.K_DOWN]:
            self.y_change += self.velocity
            self.facing = 'down'

        current_x = self.rect.x // TILE_SIZE # updates x&y position 
        current_y = self.rect.y // TILE_SIZE

        #think we could use current_tile to save to memory for when reopening game but idk ? 
        current_tile = self.game.tilemap[current_y][current_x]

        if current_tile == 'X':
            # Here you can choose which tilemap to switch to
            if self.game.tilemap == tilemap1[0] or self.game.tilemap == tilemap1[1] or self.game.tilemap == tilemap1[2] or self.game.tilemap == tilemap1[3]:
                self.game.changeMap(tilemap[1]) 
            
        elif current_tile == '1':    #HCB PATH
            if self.game.tilemap == tilemap[0] or self.game.tilemap == tilemap[1]:    #from spawn to HCB
                self.game.changeMap(tilemap1[0])
            elif self.game.tilemap == tilemap2[0] or self.game.tilemap == tilemap2[1]:                                  #from union to HCB path
                self.game.changeMap(tilemap1[2])
            elif self.game.tilemap == tilemap4[0] or self.game.tilemap == tilemap4[1] or self.game.tilemap == tilemap4[2]:
                self.game.changeMap(tilemap1[3])

        elif current_tile == '2':   #Path to union
            if self.game.tilemap == tilemap1[0] or self.game.tilemap == tilemap1[1] or self.game.tilemap == tilemap1[2] or self.game.tilemap == tilemap1[3]:
                self.game.changeMap(tilemap2[0])
            elif self.game.tilemap == tilemap3:
                self.game.changeMap(tilemap2[1])

        elif current_tile == '3':   #Union
            if self.game.tilemap == tilemap2[0] or tilemap2[1]:
                self.game.changeMap(tilemap3)

        elif current_tile == '4':   #Statue area
            if self.game.tilemap == tilemap1[0] or self.game.tilemap == tilemap1[1] or self.game.tilemap == tilemap1[2] or self.game.tilemap == tilemap1[3]:
                self.game.changeMap(tilemap4[0])
            elif self.game.tilemap == tilemap5[0] or self.game.tilemap == tilemap5[1]:
                self.game.changeMap(tilemap4[1])
            elif self.game.tilemap == tilemap7[0] or self.game.tilemap == tilemap7[1]:
                self.game.changeMap(tilemap4[2])

        elif current_tile == '5':   #Path to HWC
            if self.game.tilemap == tilemap4[0] or self.game.tilemap == tilemap4[1] or self.game.tilemap == tilemap4[2]:
                self.game.changeMap(tilemap5[0])
            elif self.game.tilemap == tilemap6:
                self.game.changeMap(tilemap5[1])
            

        elif current_tile == '6':   #HWC
            if self.game.tilemap == tilemap5[0] or self.game.tilemap == tilemap5[1]:
                self.game.changeMap(tilemap6)
        
        elif current_tile == '7':
            if self.game.tilemap == tilemap4[0] or self.game.tilemap == tilemap4[1] or self.game.tilemap == tilemap4[2]:
                self.game.changeMap(tilemap7[0])
            elif self.game.tilemap == tilemap8[0] or self.game.tilemap == tilemap8[1] or self.game.tilemap == tilemap8[2]:
                self.game.changeMap(tilemap7[1])
            elif self.game.tilemap == tilemap_hide1[0] or self.game.tilemap == tilemap_hide1[1]:
                self.game.changeMap(tilemap7[2])

        elif current_tile == '8':
            if self.game.tilemap == tilemap7[0] or self.game.tilemap == tilemap7[1]:
                self.game.changeMap(tilemap8[0])
            elif self.game.tilemap == tilemap9[0] or self.game.tilemap == tilemap9[1]:
                self.game.changeMap(tilemap8[1])
            elif self.game.tilemap == tilemap11[0] or self.game.tilemap == tilemap11[1] or self.game.tilemap == tilemap11[2]:
                self.game.changeMap(tilemap8[2])

        elif current_tile == '9':
            if self.game.tilemap == tilemap8[0] or self.game.tilemap == tilemap8[1]or self.game.tilemap == tilemap8[2]:
                self.game.changeMap(tilemap9[0])
            elif self.game.tilemap == tilemap10:
                self.game.changeMap(tilemap9[1])

        elif current_tile == '*':   #10
            if self.game.tilemap == tilemap9[0] or self.game.tilemap == tilemap9[1]:
                self.game.changeMap(tilemap10)

        elif current_tile == '+':   #11
            if self.game.tilemap == tilemap8[0] or self.game.tilemap == tilemap8[1] or self.game.tilemap == tilemap8[2]:
                self.game.changeMap(tilemap11[0])
            elif self.game.tilemap == tilemap12[0] or self.game.tilemap == tilemap12[1]:
                self.game.changeMap(tilemap11[1])
            elif self.game.tilemap == tilemap_hide1[0] or self.game.tilemap == tilemap_hide1[1]:
                self.game.changeMap(tilemap11[2])

        elif current_tile == '=':   #12
            if self.game.tilemap == tilemap11[0] or self.game.tilemap == tilemap11[1] or self.game.tilemap == tilemap11[2]:
                self.game.changeMap(tilemap12[0])
            elif self.game.tilemap == tilemap13:
                self.game.changeMap(tilemap12[1])
                
        elif current_tile == '-':
            if self.game.tilemap == tilemap12[0] or self.game.tilemap == tilemap12[1]:
                self.game.changeMap(tilemap13)

        elif current_tile == 'h':
            if self.game.tilemap == tilemap11[0] or self.game.tilemap == tilemap11[1] or self.game.tilemap == tilemap11[2]:
                self.game.changeMap(tilemap_hide1[0])
            elif self.game.tilemap == tilemap7[2]:
                self.game.changeMap(tilemap_hide1[1])
            
            
        #battle schemantics 
        if (current_tile == '.' and self.facing != 'battle' and random.randint(1,300) == 1):
            self.trigger_battle("WILD")

    def trigger_battle(self, battleType, enemyParty=[]):
        print("A WILD POKEMON APPEARS!") #this will be on the actual game screen, just for testing purposes 
        self.facing = 'battle' # self facing battle lets us change 
        if battleType=="WILD":
            pokemon_battling = random.randint(1,148)
            print(pokemon_battling)
            wild_pokemon = []
            wild_pokemon.append((copy.copy(pokedex.Pokedex[pokemon_battling-1])))
            battleTest.Battle(self.playerPokemon, wild_pokemon, battleType)
        elif battleType == "TRAINER":
            battleTest.Battle(self.playerPokemon, enemyParty, "TRAINER")
        
        # battleTest.Battle()
        # change battle screen 

    #accounts for what tiles you are on, changes accordingly        
    def npc_collision(self,direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.enemies, False)   
            if hits:
                if self.x_change > 0:   #moving right
                    self.rect.x = hits[0].rect.left - self.rect.width   #moves player back to point of collision instead of moving inside block
                if self.x_change < 0:   #moving left
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
            # print(self.game.enemies)
            if hits:
                if self.y_change > 0:   #moving down
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:   #moving up
                    self.rect.y = hits[0].rect.bottom

    def tile_collision(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)   
            if hits:
                if self.x_change > 0:   #moving right
                    self.rect.x = hits[0].rect.left - self.rect.width   #moves player back to point of collision instead of moving inside block
                if self.x_change < 0:   #moving left
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:   #moving down
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:   #moving up
                    self.rect.y = hits[0].rect.bottom

    def update(self,events):                       #check for key press for every update
        self.movement()
        self.rect.x += self.x_change
        self.tile_collision('x')
        self.npc_collision('x')
        self.rect.y += self.y_change
        self.tile_collision('y')
        self.npc_collision('y')
        self.x_change = 0
        self.y_change = 0
        
        #game update for after battle occurs
        if(self.facing == 'battle'):
            # battleTest.Battle()
            self.facing = 'down'

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))  #third parameter is tuple to select certain snippet of sprite from image file
        sprite.set_colorkey(BLACK)
        return sprite
    
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        #self.image = pygame.transform.scale(pygame.image.load("images/boulder.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)        #rocks
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        self.image = pygame.transform.scale(pygame.image.load("images/wall.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        #self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)        #rocks
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

class Stop(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        self.image = pygame.transform.scale(pygame.image.load("images/do_not_enter.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        #self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)        #rocks
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
        
class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        #self.image = pygame.transform.scale(pygame.image.load("images/boulder.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        self.image = self.game.terrain_spritesheet.get_sprite(935, 646, self.width, self.height)    #stone pathway
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

class Lava(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        #self.image = pygame.transform.scale(pygame.image.load("images/boulder.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        self.image = self.game.terrain_spritesheet.get_sprite(511, 96, self.width, self.height)    #stone pathway
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        #self.image = pygame.transform.scale(pygame.image.load("images/boulder.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        self.image = self.game.terrain_spritesheet.get_sprite(899, 98, self.width, self.height)    #stone pathway
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

class Zapdos(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        self.image = pygame.transform.scale(pygame.image.load("images/zapdos.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        #self.image = self.game.terrain_spritesheet.get_sprite(935, 646, self.width, self.height)    #stone pathway
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

class Articuno(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        self.image = pygame.transform.scale(pygame.image.load("images/articuno.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        #self.image = self.game.terrain_spritesheet.get_sprite(935, 646, self.width, self.height)    #stone pathway
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

class Moltres(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE
        self.image = pygame.transform.scale(pygame.image.load("images/moltres.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        #self.image = self.game.terrain_spritesheet.get_sprite(935, 646, self.width, self.height)    #stone pathway
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

    
class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y* TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Floor(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILE_SIZE
        self.y = y* TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = self.game.terrain_spritesheet.get_sprite(117, 453, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

