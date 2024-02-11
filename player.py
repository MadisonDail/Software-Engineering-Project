from entity import *
import pygame

class Player(Entity):                       #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen):
        super().__init__(id,game,layer,x,y,spriteImage,screen)

    def movement(self):                     #adjust sprite position if a key is pressed
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if key_press[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if key_press[pygame.K_UP]:
            self.rect.y -= self.velocity
        if key_press[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def update(self):                       #check for key press for every update
        self.movement()

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

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
        