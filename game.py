import pygame
from config import *
from player import *
from NPC import *
from Trainer import *
from Nurse import *
from dialog import *
import sys
class Game:
    def __init__(self):
        pygame.init()   #initializing pygame
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))      #creates window for game. parameters are tuple of map dimensions (in pixels)
        self.clock = pygame.time.Clock()    #sets framerate
        #self.font = pygame.font.Font('Arial', 32)   #in-game font
        self.tilemap = tilemap #added for collision detection 
        self.running = True     #whether the game should be running or not (set to true on new game)
        self.character_locations = {} 
        self.character_locations["trainer"] = []
        self.terrain_spritesheet = Spritesheet('images/img/img/terrain.png')
        self.isDialogTriggered = False
        self.Dialog = Dialog(self,DIALOG_LAYER,self.screen,0)
        self.events_of_loop = []
        self.isEncountered = False

    def createTilemap(self):
        for i, row in enumerate(self.tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)   #Creates block at position (j,i)
                elif column == "P":
                    self.setplayer(j,i) #create player at position (j,i) 
                elif column == "U":     #store trainer locations along with facing direction(ex. U is up)
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"up"])
                elif column == "R":
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"right"])
                elif column == "D":
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"down"])
                elif column == "L":
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"left"])
                elif column == "N":
                    self.character_locations["nurse"] = [j,i]
                    # NPC("npc",self,PLAYER_LAYER,j,i,player_image,self.screen,self.player)      
                elif column == "X":
                    pass #Door(j, i, layer, nextscreen)     #creates tile that moves player to other screen/area
    #changes map

    def setplayer(self,j,i):
        self.player = Player("player", self, PLAYER_LAYER, j, i, player_image,self.screen) 

    def setNurse(self):
        if len(self.character_locations["nurse"]) != 0:
            Nurse("nurse",self,PLAYER_LAYER,self.character_locations["nurse"][0],self.character_locations["nurse"][1],trainer_image,self.screen,self.player)

    def changeMap(self, newtilemap):
        self.tilemap = newtilemap
        self.all_sprites.empty() 
        self.blocks.empty()
        #both get emptied to account for new ones in diff map generation
        self.character_locations["trainer"] = []
        self.character_locations["nurse"] = []
        self.createTilemap() 
        self.setTrainers()
        self.setNurse()

        #displays new map on screen

    def setTrainers(self):
        list_of_trainer_locations = self.character_locations["trainer"]
        for count,loc in enumerate(list_of_trainer_locations):
            Trainer("trainer_"+str(count),self,PLAYER_LAYER,loc[0],loc[1],trainer_image,self.screen,self.player,loc[2])

    def new(self):
        #new game starts
        self.playing = True
        self.isFirstGeneration = False

        self.all_sprites = pygame.sprite.LayeredUpdates()       #contains all game sprites (player, NPCs, etc.)
        self.blocks = pygame.sprite.LayeredUpdates()        #object containing all of the borders/walls
        self.enemies = pygame.sprite.LayeredUpdates()       #contains enemies
        self.createTilemap()
        self.setTrainers()
        self.setNurse()

            
        # self.trainer = Trainer("trainer_1",self,PLAYER_LAYER,self.character_locations["trainer"][0],self.character_locations["trainer"][1],trainer_image,self.screen,self.player,"up")
        # self.npc = NPC("npc",self,PLAYER_LAYER,self.character_locations["npc"][0],self.character_locations["npc"][1],nurse_image,self.screen,self.player)

    def events(self,events):   #any event (any key pressed events)
        for event in events:        #gets every event that happens in pygame
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self,events):   #updates image
        # self.all_sprites.update(events)       #finds update method in every sprite object 
        list_of_returns = []
        for sprite in self.all_sprites:
            return_val = sprite.update(events)
            list_of_returns.append([sprite,return_val])

        if not self.isDialogTriggered:   
            first_triggered = False                 #make it so only first dialog trigger is done
            for return_sprite in list_of_returns:   #loop through list where first index is object and second index is return
                if return_sprite[1] == True and not first_triggered:
                    self.isDialogTriggered = True
                    print(return_sprite[0])
                    self.Dialog = Dialog(self,DIALOG_LAYER,self.screen,return_sprite[0])
                    first_triggered = True

        

    def draw(self):     #displays sprites and textures
        self.all_sprites.draw(self.screen)      #calls draw method which looks through every sprite and draws correct ones
        
        if self.isDialogTriggered:
            if not self.isEncountered:
                self.Dialog.draw(self.screen)
                self.isEncountered = True
            else:
                for event in self.events_of_loop:
                    if event.type == pygame.MOUSEBUTTONUP:                  #if user clicks on dialog box      
                        if self.Dialog.get_rect().collidepoint(event.pos):
                            self.isEncountered = self.Dialog.next_dialog()  #isEncountered will be set to false when there is not more dialog left in list
                            if self.isEncountered:                          #draw next dialog
                                self.Dialog.draw(self.screen)
                if self.isEncountered:                   
                    self.Dialog.draw(self.screen)
                    self.player.stop_movement()
                else:
                    self.isDialogTriggered = False
                    self.player.resume_movement()

        self.clock.tick(FPS)        #update screen at 60fps
        pygame.display.update()     #updates screen

    def main(self):
        #game loop
        while self.playing:
            self.screen.fill(BLACK)
            self.events_of_loop = pygame.event.get()
            self.events(self.events_of_loop)
            self.update(self.events_of_loop)
            self.draw()
        self.running = False

    def game_over(self):
        pass

    # def intro_screen(self):