from entity import *
import pygame
import random  #battle encounters 
class Player(Entity):                       #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen):
        super().__init__(id,game,layer,x,y,spriteImage,screen)
        self.x_change = 0   #temp variable to be added to coordinated in update
        self.y_change = 0
        self.facing = 'down'

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
            self.game.changeMap(tilemap)

        elif current_tile == '0':
            self.game.changeMap(tilemap0)

        elif current_tile == '1':
            self.game.changeMap(tilemap1)

        elif current_tile == '2':
            self.game.changeMap(tilemap2)

        elif current_tile == '3':
            self.game.changeMap(tilemap3)
            
        #battle schemantics 
        if (current_tile == '.' and self.facing != 'battle' and random.randint(1,100) == 1):
            self.trigger_battle()

    def trigger_battle(self):
        print("A WILD POKEMON APPEARS!") #this will be on the actual game screen, just for testing purposes 
        self.facing = 'battle' # self facing battle lets us change 
        # change battle screen 

    #accounts for what tiles you are on, changes accordingly        
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

    def update(self):                       #check for key press for every update
        self.movement()
        self.rect.x += self.x_change
        self.tile_collision('x')
        self.rect.y += self.y_change
        self.tile_collision('y')
        self.x_change = 0
        self.y_change = 0
        
        #game update for after battle occurs
        if(self.facing == 'battle'):
            self.facing = 'down'

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
        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
        

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))  #third parameter is tuple to select certain snippet of sprite from image file
        sprite.set_colorkey(BLACK)
        return sprite
    
class Ground(pygame.sprite.Sprite):
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