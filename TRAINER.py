from entity import *
import pygame
import dialog

class TRAINER(Entity):                       #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player,facing_direction):
        self.player = player
        self.dialog = dialog.Dialog()
        self.facing_direction = facing_direction
        self.isEncountered = False
        self.isDefeated = False
        super().__init__(id,game,layer,x,y,spriteImage,screen)


    def update(self,events):                                                       #check for mouse click for every update
        if self.isDefeated == False and self.isEncountered == False:               #if trainer has not been defeated yet check if player is in line of sight
            if self.facing_direction == "up":
                if (self.player.rect.y < self.rect.y) and (self.player.rect.x < self.rect.x):        #if player is above the trainer and if player horizonal location is past the trainer
                    self.dialog.draw(self.screen)
                    self.isEncountered = True

            # elif self.facing_direction == "down":

            # elif self.facing_direction == "right":      #if facing right

            # else:                                       #if facing left
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.dialog.get_rect().collidepoint(event.pos):
                        self.isEncountered = False
                        
            if self.isEncountered:
                self.dialog.draw(self.screen)


                
                