import pygame
from entity import *
from config import *

class Dialog(Entity):
    def __init__(self):
        self.dialog_index = 0
        self.font = pygame.font.SysFont('Comic Sans', 20)
        self.text = []
        self.count = 0
        self.is_rendered = False
        self.save_render = {}


    def draw(self,screen):

        if self.is_rendered == False:           #when dialog is first trigger, render with text animation
            self.render_dialog_box(screen)
            self.render_text(screen)
            self.is_rendered = True             #once dialog and text are rendered
            self.constant_display(screen)
            print(self.text[self.count])
        else:                                   #keep dialog on screen 
            self.render_dialog_box(screen)
            screen.blit(self.save_render['t'],(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))
            
    
    def render_dialog_box(self,screen):     #draw rectangle to act as dialog box
        dialogbox = pygame.draw.rect(screen,GARNET,pygame.Rect(DIALOG_BOX_X,DIALOG_BOX_Y,DIALOG_BOX_WIDTH,DIALOG_BOX_HEIGHT),0,10)
        pygame.draw.rect(screen,GOLD,dialogbox,3,10) 
        

    def render_text(self,screen):                     #draw text onto location
        for i in range(len(self.text[self.count])+1): #loop prints text letter by letter
            screen.blit(self.font.render(self.text[self.count][:i],False,GOLD),(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))
            pygame.display.update(pygame.Rect(DIALOG_BOX_X, DIALOG_BOX_Y, DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT)) #update only dialog box area
            pygame.time.wait(50)

    def constant_display(self,screen):
        self.save_render['t'] = self.font.render(self.text[self.count],False,GOLD)
        screen.blit(self.save_render['t'],(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))
        pygame.display.update(pygame.Rect(DIALOG_BOX_X, DIALOG_BOX_Y, DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT))     #update only dialog box area

    def get_rect(self):
        return pygame.Rect(DIALOG_BOX_X, DIALOG_BOX_Y, DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT)
    
    def set_dialog_text(self,list_of_dialog=["default_text"]):
        for text in list_of_dialog:
            self.text.append(text)
        print(self.text)

    def next_dialog(self):          #return true if there is more dialog, else false
        if self.count+1 == len(self.text):
            return False            #if all dialog in text list is gone through
        else:
            self.is_rendered = False
            self.count +=1          #go to next dialog 
            return True



