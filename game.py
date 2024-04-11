import pygame
from config import *
from player import *
import sys
class Game:
    def __init__(self):
        pygame.init()   #initializing pygame
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))      #creates window for game. parameters are tuple of map dimensions (in pixels)
        self.clock = pygame.time.Clock()    #sets framerate
        #self.font = pygame.font.Font('Arial', 32)   #in-game font
        self.tilemap = tilemap #added for collision detection 
        self.running = True     #whether the game should be running or not (set to true on new game)

        self.terrain_spritesheet = Spritesheet('images/img/img/terrain.png')

    def createTilemap(self):
        for i, row in enumerate(self.tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)   #Creates block at position (j,i)
                elif column == "P":
                    Player("player", self, PLAYER_LAYER, j, i, player_image,self.screen)        
                elif column == "X":
                    pass #Door(j, i, layer, nextscreen)     #creates tile that moves player to other screen/area
    #changes map
    def changeMap(self, newtilemap):
        self.tilemap = newtilemap
        self.all_sprites.empty() 
        self.blocks.empty()
        #both get emptied to account for new ones in diff map generation
        self.createTilemap() 
        #displays new map on screen

    def new(self):
        #new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()       #contains all game sprites (player, NPCs, etc.)
        self.blocks = pygame.sprite.LayeredUpdates()        #object containing all of the borders/walls
        self.enemies = pygame.sprite.LayeredUpdates()       #contains enemies
        self.createTilemap()

    def events(self):   #any event (any key pressed events)
        for event in pygame.event.get():        #gets every event that happens in pygame
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):   #updates image
        self.all_sprites.update()       #finds update method in every sprite object 

    def draw(self):     #displays sprites and textures
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)      #calls draw method which looks through every sprite and draws correct ones
        self.clock.tick(FPS)        #update screen at 60fps
        pygame.display.update()     #updates screen

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
        self.running = False

    def game_over(self):
        pass

    # def intro_screen(self):