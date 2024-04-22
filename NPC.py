from entity import *
import pygame

class NPC(Entity):                                  #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player):
        self.player = player
        super().__init__(id,game,layer,x,y,spriteImage,screen)
                    