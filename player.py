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

    def update(self,events):                #check for key press for every update
        self.movement()

    def stop_movement(self):                #don't allow player sprite to move
        self.velocity = 0
    
    def resume_movement(self, vel=DEFAULT_SPEED):
        self.velocity = vel                 #allow player to move again