import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite): # inherits from pygame.sprite.Sprite
    def __init__(self, game, x, y): # Constructor method for the Player class
        self.game = game # Reference to the game instance
        self._layer = PLAYER_LAYER # Set the layer of the sprite
        self.groups = self.game.all_sprites # Assign the sprite to the 'all_sprites' group
        pygame.sprite.Sprite.__init__(self, self.groups) # Call the constructor of the parent class

        # Initialize player position and dimensions
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        # Create a surface for the player and fill it with a color
        self.image = pygame.Surface([self.width, self.height]) 
        self.image.fill(RED) 

        # Create a rectangle to represent the player's position and dimensions
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self): # Update method, currently empty as there is no specific update logic for the player
        pass
