import pygame
from entity import *
from config import *
from NPC import *
from Trainer import Trainer
from Nurse import Nurse

class Dialog():
    def __init__(self,game,layer,screen,object_type,x=DIALOG_BOX_X,y=DIALOG_BOX_Y):
        self.dialog_index = 0
        self.font = pygame.font.SysFont('Comic Sans', 20)
        self.text = ["test",["check",["lol","no"]]]
        self.count = 0
        self.is_rendered = False
        self.save_render = {}
        self.currentoptions = []
        self.events = 0
        self._layer = DIALOG_LAYER
        self.option_rects = []
        self.option_func_trigger = []
        self.is_option = False              #set to True in instance check if first item in list is an dialog that has options

        print('in dialog init:')
        # print(object_type)
        if isinstance(object_type,Trainer):
            self.text = ["Let's battle!",["test",['y','n']]]
            # self.option_func_trigger = [[0,'exitdialog']]
        elif isinstance(object_type,Nurse):
            self.is_option = True
            self.text = [["Would you like me to heal you pokemon?",['y','n']]]
            self.option_func_trigger = [['healallpoke','exitdialog']]            #length of func_triggers should be equal to length of self.text


    def trigger_option_func(self,index_of_trigger):
        temp = self.option_func_trigger[self.count]
        func_triggered = temp[index_of_trigger]
        # print('hi')
        # print(func_triggered)
        if func_triggered == 'exitdialog':
            self.count = len(self.text)-1             #exit dialog will make it so dialog quits
            return False                              #set count to largest index and return False to end dialog
        #elif .... add more checks here

        return True                                   


    def draw(self,screen):
        if self.is_rendered == False:           #when dialog is first trigger, render with text animation
            self.render_dialog_box(screen)
            if isinstance(self.text[self.count],list):
                text,self.currentoptions = self.detect_options()
                self.render_text(screen,text)
                self.is_rendered = True             #once dialog and text are rendered
                self.display_options(screen,self.currentoptions,True)
                self.constant_display(screen,text)
            else:
                self.is_option = False
                self.render_text(screen,self.text[self.count])
                self.is_rendered = True             #once dialog and text are rendered
                self.constant_display(screen,self.text[self.count])
            # print(self.text[self.count])
        else:                                   #keep dialog on screen 
            if isinstance(self.text[self.count],list):
                self.display_options(screen,self.currentoptions,False)
            self.render_dialog_box(screen)
            screen.blit(self.save_render['t'],(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))
            
    
    def render_dialog_box(self,screen):     #draw rectangle to act as dialog box
        dialogbox = pygame.draw.rect(screen,GARNET,pygame.Rect(DIALOG_BOX_X,DIALOG_BOX_Y,DIALOG_BOX_WIDTH,DIALOG_BOX_HEIGHT),0,10)
        pygame.draw.rect(screen,GOLD,dialogbox,3,10) 
        

    def render_text(self,screen,text):                      #draw text onto location
        screen.blit(self.font.render(text,False,GOLD),(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))

    def constant_display(self,screen,text):
        self.save_render['t'] = self.font.render(text,False,GOLD)
        screen.blit(self.save_render['t'],(DIALOG_BOX_X+DIALOG_BOX_MARGIN,DIALOG_BOX_Y+DIALOG_BOX_MARGIN))
        # pygame.display.update(pygame.Rect(DIALOG_BOX_X, DIALOG_BOX_Y, DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT))     #update only dialog box area

    def get_rect(self):
        return pygame.Rect(DIALOG_BOX_X, DIALOG_BOX_Y, DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT)
    
    def set_dialog_text(self,list_of_dialog=["default_text"]):
        for text in list_of_dialog:
            self.text.append(text)
        # print(self.text)

    def next_dialog(self):          #return true if there is more dialog, else false
        self.currentoptions = []
        if self.count+1 == len(self.text):
            return False            #if all dialog in text list is gone through
        else:
            self.is_rendered = False
            self.count +=1          #go to next dialog 
            return True
        
    # def is_dialog_option(self):
    #     return self.is_option
    
    def display_options(self,screen,options,firstload):
        num_of_options = len(options)
        dialogbox = pygame.draw.rect(screen,GARNET,pygame.Rect(DIALOG_OPTION_X,DIALOG_OPTION_Y-(DIALOG_OPTION_HEIGHT*(num_of_options-1)),DIALOG_OPTION_WIDTH,DIALOG_OPTION_HEIGHT*num_of_options),0,10)
        pygame.draw.rect(screen,GOLD,dialogbox,3,10) 
        isrend = False
        for count,option in enumerate(options):
            if pygame.mouse.get_focused() != 0:         #if mouse is not outside of screen
                temprect = pygame.Rect(DIALOG_OPTION_X+DIALOG_BOX_MARGIN,DIALOG_OPTION_Y-(DIALOG_OPTION_HEIGHT*(num_of_options-1-count))+DIALOG_BOX_MARGIN,DIALOG_OPTION_WIDTH,DIALOG_OPTION_HEIGHT)
                if temprect.collidepoint(pygame.mouse.get_pos()):       #if mouse is over a certain option, adjust color to indicate so
                    screen.blit(self.font.render(option,False,SELECTGOLD),(DIALOG_OPTION_X+DIALOG_BOX_MARGIN,DIALOG_OPTION_Y-(DIALOG_OPTION_HEIGHT*(num_of_options-1-count))+DIALOG_BOX_MARGIN,DIALOG_OPTION_WIDTH,DIALOG_OPTION_HEIGHT))
                    isrend = True
            if firstload:                               #save option rect in to self.option_rects
                self.option_rects.append(pygame.Rect(DIALOG_OPTION_X+DIALOG_BOX_MARGIN,DIALOG_OPTION_Y-(DIALOG_OPTION_HEIGHT*(num_of_options-1-count))+DIALOG_BOX_MARGIN,DIALOG_OPTION_WIDTH,DIALOG_OPTION_HEIGHT))
            if not isrend:
                screen.blit(self.font.render(option,False,GOLD),(DIALOG_OPTION_X+DIALOG_BOX_MARGIN,DIALOG_OPTION_Y-(DIALOG_OPTION_HEIGHT*(num_of_options-1-count))+DIALOG_BOX_MARGIN,DIALOG_OPTION_WIDTH,DIALOG_OPTION_HEIGHT))
            isrend = False
        # print(self.option_rects)

    def detect_options(self):
        self.is_option = True
        dialogtext = self.text[self.count][0]
        options = self.text[self.count][1]
        return dialogtext,options
    
    def getevents(self,events):
        self.events = events

    def reset_dialog(self):
        self.count = 0
        self.is_rendered = False

