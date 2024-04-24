import pygame
from config import *
from player import *
from NPC import *
from Trainer import *
from Nurse import *
import dialog
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
        self.terrain_spritesheet = Spritesheet('images/img/img/terrain.png')
        self.isFirstGeneration = True 

    def createTilemap(self):
        for i, row in enumerate(self.tilemap):
            for j, column in enumerate(row):
                #different backgrounds
                if self.tilemap == tilemap:
                    Grass(self, j, i)
                elif self.tilemap == tilemap4:
                    Path(self, j, i)
                    
              
                if column == "B":
                    Block(self, j, i)   #Creates block at position (j,i)
                elif column == "P":
                    self.character_locations["player"] = [j,i]
                    # if not self.isFirstGeneration:
                    #     self.player.set_position(j,i)
                    # Player("player", self, PLAYER_LAYER, j, i, player_image,self.screen)        #create player at position (j,i) 
                elif column == "T":
                    self.character_locations["trainer"] = [j,i]
                    # TRAINER("trainer_1",self,PLAYER_LAYER,j,i,player_image,self.screen,self.player,"up")
                # elif column == "N":
                #     self.character_locations["nurse"] = [j,i]
                    # NPC("npc",self,PLAYER_LAYER,j,i,player_image,self.screen,self.player)      
                elif column == "X":
                    pass #Door(j, i, layer, nextscreen)     #creates tile that moves player to other screen/area
    #changes map
    def changeMap(self, newtilemap):
        self.tilemap = newtilemap
        self.all_sprites.empty() 
        self.blocks.empty()
        self.player = Player("player", self, PLAYER_LAYER, self.character_locations["player"][0], self.character_locations["player"][1], player_image,self.screen) 
        #both get emptied to account for new ones in diff map generation
        self.createTilemap() 
        #displays new map on screen

    def new(self):
        #new game starts
        self.playing = True
        self.isFirstGeneration = False

        self.all_sprites = pygame.sprite.LayeredUpdates()       #contains all game sprites (player, NPCs, etc.)
        self.blocks = pygame.sprite.LayeredUpdates()        #object containing all of the borders/walls
        self.enemies = pygame.sprite.LayeredUpdates()       #contains enemies
        self.createTilemap()
        self.player = Player("player", self, PLAYER_LAYER, self.character_locations["player"][0], self.character_locations["player"][1], player_image,self.screen) 
        self.trainer = Trainer("trainer_1",self,PLAYER_LAYER,self.character_locations["trainer"][0],self.character_locations["trainer"][1],trainer_image,self.screen,self.player,"up")
        # self.npc = NPC("npc",self,PLAYER_LAYER,self.character_locations["npc"][0],self.character_locations["npc"][1],nurse_image,self.screen,self.player)

    def events(self,events):   #any event (any key pressed events)
        for event in events:        #gets every event that happens in pygame
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self,events):   #updates image
        self.all_sprites.update(events)       #finds update method in every sprite object 

    def draw(self):     #displays sprites and textures
        self.all_sprites.draw(self.screen)      #calls draw method which looks through every sprite and draws correct ones
        self.clock.tick(FPS)        #update screen at 60fps
        pygame.display.update()     #updates screen

    def main(self):
        #game loop
        while self.playing:
            self.screen.fill(BLACK)
            events_of_loop = pygame.event.get()
            self.events(events_of_loop)
            self.update(events_of_loop)
            self.draw()
        self.running = False

    def game_over(self):
        pass

    # def intro_screen(self):