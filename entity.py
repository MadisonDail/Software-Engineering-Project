import pygame
RED = (255,0,0)

class Entity(pygame.sprite.Sprite):
    def __init__(self,id,x,y,spriteImage):  #store id, x and y position, and sprite image
        super().__init__()
        self.id = id
        self.position = [x,y]
        self.speed = 0
        self.image = pygame.transform.scale(pygame.image.load(spriteImage),(100,100))   #scale image size to 100x100
        self.rect = self.image.get_rect()   #set rectangle to the image
        self.rect.center = (x,y)            #center of rectangle(x and y coords)

    def show_hitbox(self,screen):
        pygame.draw.rect(screen,RED,self.rect,1)                   


class Player(Entity):                       #inherit from entity
    def __init__(self,id,x,y,spriteImage):
        super().__init__(id,x,y,spriteImage)

    # def movement_controls(self):
    #     key_press = pygame.key.get_pressed()
    #     if key_press[pygame.K_LEFT]:



