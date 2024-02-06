import pygame
RED = (255,0,0)

class Entity(pygame.sprite.Sprite):
    def __init__(self,id,x,y,spriteImage,screen):  #store id, x and y position, and sprite image
        super().__init__()
        self.id = id
        self.position = [x,y]
        self.velocity = 5
        self.image = pygame.transform.scale(pygame.image.load(spriteImage),(100,100))   #scale image size to 100x100
        self.rect = self.image.get_rect()   #set rectangle to the image
        self.rect.center = (x,y)            #center of rectangle(x and y coords)
        self.screen = screen

        self.hitbox = pygame.draw.rect(self.image,RED,self.image.get_rect(),1)          #show rect border of entity                  


class Player(Entity):                       #inherit from entity
    def __init__(self,id,x,y,spriteImage,screen):
        super().__init__(id,x,y,spriteImage,screen)

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



