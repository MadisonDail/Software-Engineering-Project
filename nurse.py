from entity import *
import pygame

class NurseNPC(Entity):
    def __init__(self, id, game, layer, x, y, spriteImage, screen):
        super().__init__(id, game, layer, x, y, spriteImage, screen)
        self.dialog_text = ['Welcome to the FSU Pokemon Center!',
                            'What can I help you with?',
                            'Okay!']
    