from entity import *
import pygame
import dialog
from NPC import *

class Nurse(NPC):                       #inherit from NPC
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player,facing_direction):
        self.facing_direction = facing_direction
        self.dialog = dialog.Dialog()
        
        super().__init__(self,id,game,layer,x,y,spriteImage,screen,player)

    def update(self,events):                       #check for mouse click for every update
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos) and abs(self.player.rect.x-self.rect.x) < 64:
                    self.dialog.draw(self.screen)

    # def set_dialog(self):
    #     self.dialog