import pygame
from entity import *
from config import *
from NPC import *
from Trainer import Trainer
from Nurse import Nurse
import player
import battleTest

class Dialog():
    def __init__(self,game,layer,screen,object_type,x=DIALOG_BOX_X,y=DIALOG_BOX_Y,text=["test",["check",["lol","no"]]]):
        self.dialog_index = 0
        self.font = pygame.font.SysFont('Comic Sans', 20)
        self.text = text
        self.count = 0
        self.is_rendered = False
        self.save_render = {}
        self.currentoptions = []
        self.events = 0
        self._layer = DIALOG_LAYER
        self.option_rects = []
        self.option_func_trigger = []
        self.is_option = False              #set to True in instance check if first item in list is an dialog that has options
        self.object_type = object_type
        self.multiple_paths_select = -1

        print('in dialog init:')
        # print(object_type)
        if isinstance(object_type,Trainer):
            self.text = ['Let\'s battle!',['Come on!',['Fine.','No!']],{1:'Haha! You lost!',2:'You\'ve won!'}]
            # self.text = ['Let\'s battle!',['Come on!',['Fine.','No!']]]
            self.is_multiple_paths = True
            self.option_func_trigger = [[],['battle','exitdialog'],[],[]]
            object_type.player.isInBattle = True
        elif isinstance(object_type,Nurse):
            self.is_option = True
            self.text = [['Would you like me to heal your pokemon?',['Yeah!','No thanks']],'I have healed your pokemon!']
            self.option_func_trigger = [['healallpoke','exitdialog'],[]]            #length of func_triggers should be equal to length of self.text
            object_type.player.isInBattle = True
        

    def trigger_option_func(self,index_of_trigger):
        temp = self.option_func_trigger[self.count]

        if not len(temp) == 0:                              #if the list is empty
            func_triggered = temp[index_of_trigger]
            if func_triggered == 'exitdialog':
                # self.count = len(self.text)-1             #exit dialog will make it so dialog quits
                self.object_type.player.isInBattle = False 
                self.next_dialog()
                return False                             #set count to largest index and return False to end dialog
            elif func_triggered == 'battle':              #trigger trainer battle
                # print(self.object_type)
                # print(self.object_type.party)
                self.object_type.player.trigger_battle("TRAINER", self.object_type.party)
                temp = self.object_type.player.battleVal
                print(self.object_type.id)
                print('in dia')
                print(temp)
                # self.object_type.player.isInBattle = False  #remove this once battle check is implemented
                # print(temp)
                self.multiple_paths_select = temp
                self.next_dialog()

                return True          #set to true when return is done
            elif func_triggered == 'healallpoke':
                battleTest.HealParty(self.object_type.player.playerPokemon)
                # print('attempted to heal')
                self.next_dialog()
                self.object_type.player.isInBattle = False 
                return True
            #elif .... add more checks here

        return True                                   


    def draw(self,screen):
        # print('loop')
        # print(self.count)
        if self.is_rendered == False:           #when dialog is first trigger, render with text animation
            self.render_dialog_box(screen)
            if isinstance(self.text[self.count],list):
                print('list')
                text,self.currentoptions = self.detect_options()
                self.render_text(screen,text)
                self.is_rendered = True             #once dialog and text are rendered
                self.display_options(screen,self.currentoptions,True)
                self.constant_display(screen,text)
            elif isinstance(self.text[self.count],dict):
                print('AYYY')
                print(self.text[self.count])
                temp = self.text[self.count]
                text = temp[self.multiple_paths_select]
                print(text)
                print(type(text))
                self.is_option = False
                self.render_text(screen,text)
                self.is_rendered = True             #once dialog and text are rendered
                self.constant_display(screen,text)
            else:
                self.is_option = False
                self.render_text(screen,self.text[self.count])
                print('STUFF')
                print(type(self.text[self.count]))
                print(self.text[self.count])
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
        # print('in render')
        # print(text)
        # print(type(text))
        # text = str(text)
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
        # print(self.count+1)
        # print(len(self.text))

        if self.count+1 == len(self.text):
            self.object_type.player.isInBattle = False
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

