from entity import *
import pygame
import dialog
from NPC import *

class Trainer(NPC):                       #inherit from NPC
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player,facing_direction):
        self.facing_direction = facing_direction
        self.isEncountered = False
        self.isDefeated = False
        self.dialog = dialog.Dialog(game,layer+1,screen)
        self.dialog.set_dialog_text(["You seem strong!",["Here we go!",["Yeah!","No thanks.","WHAR",'hi']], "Let's battle!"])
        self.has_encountered = False

        super().__init__(id,game,layer,x,y,spriteImage,screen,player)


    def update(self,events):                                                       #check for mouse click for every update
        if self.isDefeated == False and self.isEncountered == False and self.has_encountered == False:               #if trainer has not been defeated yet check if player is in line of sight
            if self.facing_direction == "up":
                if (self.player.rect.y+TILE_SIZE < self.rect.y) and (self.player.rect.x == self.rect.x):        #if player is above the trainer and if player horizonal location is past the trainer
                    self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
            elif self.facing_direction == "down":
                if (self.player.rect.y+TILE_SIZE > self.rect.y) and (self.player.rect.x == self.rect.x):        #if player is below the trainer and if player horizonal location is past the trainer
                    self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
            elif self.facing_direction == "right":      #if facing right
                if (self.player.rect.y == self.rect.y) and (self.player.rect.x+TILE_SIZE > self.rect.x):        #if player is to the right of the trainer and if player is horizontal to trainer
                    self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
            else:                                       #if facing left
                if (self.player.rect.y == self.rect.y) and (self.player.rect.x-TILE_SIZE < self.rect.x):        #if player is to the left of the trainer and if player is horizontal to trainer
                    self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:    #if user clicks on dialog box      
                    if self.dialog.get_rect().collidepoint(event.pos):
                        self.isEncountered = self.dialog.next_dialog()
                        if(self.isEncountered):
                            self.dialog.draw(self.screen)
                        # print("Hi")
                        # print(self.isEncountered)
                        
            if self.isEncountered:
                self.dialog.getevents(events)                       
                self.dialog.draw(self.screen)
                self.player.stop_movement()
            else:
                self.player.resume_movement()

                
                