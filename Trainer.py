from entity import *
import pygame
from NPC import NPC
import random
import pokedex

class Trainer(NPC):                       #inherit from NPC
    def __init__(self,id,game,layer,x,y,spriteImage,screen,player,facing_direction, party=[]):
        self.facing_direction = facing_direction
        self.isEncountered = False
        self.isDefeated = False
        self.has_encountered = False
        partyLen = random.randint(1,6)
        self.party = party
        if len(self.party) < partyLen:
            temp = abs(len(self.party)-partyLen)
            print(f'adding! {temp}')
            for i in range(temp):
                self.party.append(pokedex.Pokedex[random.randint(1, 151) - 1])
        print(self.party)

        super().__init__(id,game,layer,x,y,spriteImage,screen,player)
        self.game.enemies.add(self)     #add trainer to enemies group created in game.py


    def update(self,events):                                                       #check for mouse click for every update
        if self.isDefeated == False and self.isEncountered == False and self.has_encountered == False:               #if trainer has not been defeated yet check if player is in line of sight
            if self.facing_direction == "up":
                if (self.player.rect.y+TILE_SIZE < self.rect.y) and (self.player.rect.x > self.rect.x and self.player.rect.x < self.rect.x+TILE_SIZE):        #if player is above the trainer and if player horizonal location is past the trainer
                    # self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
                    return True
                # else:
                #     return False
            elif self.facing_direction == "down":
                if (self.player.rect.y+TILE_SIZE > self.rect.y) and (self.player.rect.x > self.rect.x and self.player.rect.x < self.rect.x+TILE_SIZE):        #if player is below the trainer and if player horizonal location is past the trainer
                    # self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
                    return True
            elif self.facing_direction == "right":      #if facing right
                if (self.player.rect.y > self.rect.y and self.player.rect.y < self.rect.y+TILE_SIZE) and (self.player.rect.x+TILE_SIZE > self.rect.x):        #if player is to the right of the trainer and if player is horizontal to trainer
                    # self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
                    return True
            else:                                       #if facing left
                if (self.player.rect.y > self.rect.y and self.player.rect.y < self.rect.y+TILE_SIZE) and (self.player.rect.x-TILE_SIZE < self.rect.x):        #if player is to the left of the trainer and if player is horizontal to trainer
                    # self.dialog.draw(self.screen)
                    self.isEncountered = True
                    self.has_encountered = True
                    return True

                
                