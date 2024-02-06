import pygame
from config import *

class Entity(pygame.sprite.Sprite):
    def __init__(self,id,game,layer,x,y,spriteImage,screen):  #store id, x and y position, and sprite image
        self.id = id
        self.position = [x,y]
        self.velocity = 5
        self.image = pygame.transform.scale(pygame.image.load(spriteImage),(TILE_SIZE,TILE_SIZE))   #scale image size to a tile
        self.rect = self.image.get_rect()   #set rectangle to the image
        self.rect.topleft = (x,y)           #top left of rectangle(x and y coords)

        self.screen = screen
        self.game = game
        self._layer = layer                 #set the layer the sprite will be on
        self.groups = self.game.all_sprites #assign the sprite to the 'all_sprites' group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.hitbox = pygame.draw.rect(self.image,RED,self.image.get_rect(),1)          #show rect border of entity                  

class TrainerNPC(Entity):
    def __init__(self,id,x,y,spriteImage,screen):
        super().__init__(id,x,y,spriteImage,screen)


