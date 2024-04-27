from entity import *
import pygame
from NPC import NPC

class Nurse(NPC):                       #inherit from NPC
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player,facing_direction="down"):
        self.facing_direction = facing_direction
        self.isEncountered = False

        super().__init__(id,game,layer,x,y,spriteImage,screen,player)
        self.game.enemies.add(self)     #add trainer to enemies group created in game.py

    def update(self,events):                       #check for mouse click for every update
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:  #set true when mouse clicks on nurse sprite and x of player and rect is less than tile_size
                if self.rect.collidepoint(event.pos) and abs(abs(self.player.rect.x)-abs(self.rect.x)) < TILE_SIZE*3 and abs(abs(self.player.rect.y)-abs(self.rect.y)) < TILE_SIZE*3:
                    return True
            