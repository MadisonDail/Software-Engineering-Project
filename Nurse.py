from entity import *
import pygame
import dialog
from NPC import *

class Nurse(NPC):                       #inherit from NPC
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player,facing_direction):
        self.facing_direction = facing_direction
        self.isEncountered = False
        self.dialog = dialog.Dialog()
        self.dialog.set_dialog_text([["Hello! How may I help you?",["Heal Pokemon","Leave"]]])
        super().__init__(id,game,layer,x,y,spriteImage,screen,player)

    def update(self,events):                       #check for mouse click for every update
        if not self.isEncountered:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.rect.collidepoint(event.pos) and abs(self.player.rect.x-self.rect.x) < 64:
                        self.dialog.draw(self.screen)
                        self.isEncountered = True
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:    #if user clicks on dialog box      
                    if self.dialog.get_rect().collidepoint(event.pos):
                        self.isEncountered = self.dialog.next_dialog()
                        if(self.isEncountered):
                            self.dialog.draw(self.screen)
            if self.isEncountered:
                self.dialog.getevents(events)                       
                self.dialog.draw(self.screen)
                self.player.stop_movement()
            else:
                self.player.resume_movement()
                self.dialog.reset_dialog()
            

    # def set_dialog(self):
    #     self.dialog