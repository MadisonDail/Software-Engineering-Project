from entity import *
import pygame
import dialog

class NPC(Entity):                       #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player):
        self.player = player
        self.dialog = dialog.Dialog()
        self.isClicked= False
        super().__init__(id,game,layer,x,y,spriteImage,screen)

    def update(self,events):                       #check for mouse click for every update

        if not self.isClicked:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.rect.collidepoint(event.pos) and abs(self.player.rect.x-self.rect.x) < 64:
                        self.dialog.draw(self.screen)
                        self.isClicked = True
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.dialog.get_rect().collidepoint(event.pos):
                        self.isClicked = False
                        
            if self.isClicked:
                self.dialog.draw(self.screen)
                
                    