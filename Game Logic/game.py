import pygame
from config import *
from player import *
from NPC import NPC
from Trainer import Trainer
from Nurse import *
from dialog import *
import sys
class Game:
    def __init__(self):
        pygame.init()   #initializing pygame 
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))      #creates window for game. parameters are tuple of map dimensions (in pixels)
        self.clock = pygame.time.Clock()    #sets framerate
        #self.font = pygame.font.Font('Arial', 32)   #in-game font;
        self.tilemap = tilemap[0] #added for collision detection 
        pygame.display.set_caption("Landis")
        self.running = True     #whether the game should be running or not (set to true on new game)
        self.character_locations = {} 
        self.character_locations["trainer"] = []
        self.character_locations["nurse"] = []
        self.terrain_spritesheet = Spritesheet('images/img/img/terrain.png')
        self.isDialogTriggered = False
        self.Dialog = Dialog(self,DIALOG_LAYER,self.screen,0)
        self.events_of_loop = []
        self.isEncountered = False
        self.player = None

    def createTilemap(self):
        for i, row in enumerate(self.tilemap):
            for j, column in enumerate(row):
                #different backgrounds
                Grass(self, j, i)

                    
                if column == "B":
                    Block(self, j, i)   #Creates block at position (j,i)
                elif column == "W":
                    Wall(self, j, i)
                elif column == "S":
                    Stop(self, j, i)
                elif column == "T":
                    Tile(self, j, i)   #Creates block at position (j,i)
                elif column == '#':
                    Bookshelf(self, j, i)
                elif column == "F":
                    Floor(self, j, i)
                elif column == "w":
                    Water(self, j, i)
                elif column == "P":
                    Tile(self, j, i)
                    self.setplayer(j,i) #create player at position (j,i) 
                elif column == "L":
                    Lava(self, j, i)
                elif column == "Z":
                    Zapdos(self, j, i)
                elif column == "A":
                    Articuno(self, j, i)
                elif column == "M":
                    Moltres(self, j, i)
                elif column == "U":     #store trainer locations along with facing direction(ex. U is up)
                    Tile(self, j, i)
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"up"])
                elif column == "R":
                    Tile(self, j, i)
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"right"])
                elif column == "D":
                    Tile(self, j, i)
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"down"])
                elif column == "l":
                    Tile(self, j, i)
                    temp = self.character_locations["trainer"]
                    temp.append([j,i,"left"])
                elif column == "N":
                    Tile(self, j, i)
                    self.character_locations["nurse"] = [j,i]
                    # NPC("npc",self,PLAYER_LAYER,j,i,player_image,self.screen,self.player)      
                elif column == "X" or column == '1' or column == '2' or column == '3' or column == '4' or column == '5' or column == '6' or column == '7' or column == '8' or column == '9' or column == '*' or column == '+' or column == '=' or column == '-':
                    Tile(self, j, i)
                
    #changes map

    # def setplayer(self,j,i):
    #     self.player = Player("player", self, PLAYER_LAYER, j, i, player_image,self.screen) 
    def setplayer(self, j, i):
        if self.player is not None:
            # Update the player's position without creating a new instance
            self.player.rect.topleft = (j * TILE_SIZE, i * TILE_SIZE)
        else:
            # Create the player if it doesn't exist yet
            self.player = Player("player", self, PLAYER_LAYER, j, i, player_image, self.screen)


    def setNurse(self):
        if len(self.character_locations["nurse"]) != 0:
            Nurse("nurse",self,PLAYER_LAYER,self.character_locations["nurse"][0],self.character_locations["nurse"][1],nurse_image,self.screen,self.player)

    def changeMap(self, newtilemap):
        # self.tilemap = newtilemap
        # self.all_sprites.empty() 
        # self.blocks.empty()
        # self.enemies.empty()
        # #both get emptied to account for new ones in diff map generation
        # self.character_locations["trainer"] = []
        # self.character_locations["nurse"] = []
        # self.createTilemap() 
        # self.setTrainers()
        # self.setNurse()
        self.character_locations["trainer"] = []
        self.character_locations["nurse"] = []
    
        self.tilemap = newtilemap
        # Clear all non-player sprites
        for sprite in self.all_sprites:
            if sprite != self.player:
                self.all_sprites.remove(sprite)
        self.blocks.empty()
        self.enemies.empty()
        # Repopulate the map
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
                pygame.quit()
                sys.exit() #quits game so doesnt go back to the menu screen when click x 

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
                            #=======ADD NEW VV
                            print(self.Dialog.is_option)
                            if not self.Dialog.is_option:                #if there is not a dialog option
                            #=====
                                if self.Dialog.get_rect().collidepoint(event.pos):
                                    self.isEncountered = self.Dialog.next_dialog()  #isEncountered will be set to false when there is not more dialog left in list
                                    if self.isEncountered:                          #draw next dialog
                                        self.Dialog.draw(self.screen)
                            #=====
                            else:
                                for count,option in enumerate(self.Dialog.option_rects):     #loop through all options
                                    # print(option,count)
                                    if option.collidepoint(event.pos):
                                        self.isEncountered = self.Dialog.trigger_option_func(count)
                            #=====
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
            self.events_of_loop.clear()
            self.events_of_loop = pygame.event.get()
            self.events(self.events_of_loop)
            self.update(self.events_of_loop)
            self.draw()
        self.running = False

    def game_over(self):
        pass

    # def intro_screen(self):