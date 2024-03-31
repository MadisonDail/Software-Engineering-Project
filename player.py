from entity import *
import pygame

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

        if self.game.tilemap[current_y][current_x] == 'X':
            # Here you can choose which tilemap to switch to
            self.game.changeMap(tilemap)

        elif self.game.tilemap[current_y][current_x] == '0':
            self.game.changeMap(tilemap0)

        elif self.game.tilemap[current_y][current_x] == '1':
            self.game.changeMap(tilemap1)

        elif self.game.tilemap[current_y][current_x] == '2':
            self.game.changeMap(tilemap2)

        elif self.game.tilemap[current_y][current_x] == '3':
            self.game.changeMap(tilemap3)

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
        #self.image = pygame.Surface([self.width, self.height])
        self.image = pygame.transform.scale(pygame.image.load("images/boulder.png"),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
        