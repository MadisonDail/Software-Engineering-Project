import pygame
from config import *

class Dialog():
    def __init__(self,player,entity):
        self.player = player
        self.entity = entity
        self.dialog_index = 0
        self.font = pygame.font.SysFont('Comic Sans', 25)
        self.text = ['What is up?','I think I have seen you before...']
        self.count = 0

    def draw(self,screen):
        self.render_dialog_box(screen)
        self.render_text(screen)
    
    def render_dialog_box(self,screen):     #draw rectangle to act as dialog box
        pygame.draw.rect(screen,GARNET,pygame.Rect(DIALOG_BOX_X,DIALOG_BOX_Y,DIALOG_BOX_WIDTH,DIALOG_BOX_HEIGHT))

    def render_text(self,screen):           #draw text onto location
        screen.blit(self.font.render(self.text[self.count],False,GOLD),(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))

