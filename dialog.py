import pygame
from entity import *
from config import *

class Dialog(Entity):
    def __init__(self):
        self.dialog_index = 0
        self.font = pygame.font.SysFont('Comic Sans', 25)
        self.text = ['What is up?','I think I have seen you before...']
        self.count = 0

    def draw(self,screen):
        self.render_dialog_box(screen)
        self.render_text(screen)
        pygame.time.wait(1000)
        if self.count == 0:
            self.count = 1
        else:
            self.count = 0
    
    def render_dialog_box(self,screen):     #draw rectangle to act as dialog box
        pygame.draw.rect(screen,GARNET,pygame.Rect(DIALOG_BOX_X,DIALOG_BOX_Y,DIALOG_BOX_WIDTH,DIALOG_BOX_HEIGHT))
        

    def render_text(self,screen):                   #draw text onto location
        for i in range(len(self.text[self.count])): #loop prints text letter by letter
            screen.blit(self.font.render(self.text[self.count][:i],False,GOLD),(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))
            pygame.display.update()
            pygame.time.wait(50)

