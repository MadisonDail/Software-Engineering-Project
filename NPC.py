from entity import *
import pygame
import dialog

class NPC(Entity):                                  #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player):
        self.player = player
        self.dialog = dialog.Dialog()
        self.isClicked= False
        super().__init__(id,game,layer,x,y,spriteImage,screen)

    def update(self,events):                       #check for mouse click for every update

        if not self.isClicked:
            for event in events:                        
                if event.type == pygame.MOUSEBUTTONUP:      #if sprite of NPC is clicked with mouse button and the player is less than a tile away horizontally and vertically
                    if self.rect.collidepoint(event.pos) and abs(self.player.rect.x-self.rect.x) < 64 and abs(self.player.rect.y-self.rect.y) < 64:
                        self.dialog.draw(self.screen)
                        self.isClicked = True
        else:
            for event in events:                            #when dialog is already rendered
                if event.type == pygame.MOUSEBUTTONUP:      #if mouse clicks on dialog box, remove dialog from screen
                    if self.dialog.get_rect().collidepoint(event.pos):
                        self.isClicked = False
                        
            if self.isClicked:                              #if dialog is already rendered and not clicked, continue to draw it
                self.dialog.draw(self.screen)
                
                    