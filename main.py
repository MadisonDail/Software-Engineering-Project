import pygame
from config import *
from player import *
import sys
import dialog

class Game:
    def __init__(self):
        pygame.init()   #initializing pygame
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))      #creates window for game. parameters are tuple of map dimensions (in pixels)
        self.clock = pygame.time.Clock()    #sets framerate
        #self.font = pygame.font.Font('Arial', 32)   #in-game font
        self.running = True     #whether the game should be running or not (set to true on new game)

    def new(self):
        #new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()       #contains all game sprites (player, NPCs, etc.)
        self.blocks = pygame.sprite.LayeredUpdates()        #object containing all of the borders/walls
        self.enemies = pygame.sprite.LayeredUpdates()       #contains enemies
        
        player_image = "images/player_stand.png"
        self.player = Player("player",self,PLAYER_LAYER,320,320,player_image,self.screen) #Player spawned at x:0 y:0
        
        trainer_image = "images/player_stand.png"
        self.npc = TrainerNPC("npc",self,PLAYER_LAYER,50,50,trainer_image,self.screen)
        self.enemies.add(self.npc)

    def events(self):   #any event (any key pressed events)
        for event in pygame.event.get():        #gets every event that happens in pygame
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):   #updates image
        self.all_sprites.update()       #finds update method in every sprite object 

    def draw(self):     #displays sprites and textures

        entities_collided = self.collision_detect(self.player,self.enemies)

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)      #calls draw method which looks through every sprite and draws correct ones
        
        if entities_collided:
                                                #if there is at least one entity collided with the player, display dialog
            self.temp = dialog.Dialog(self.player,self.npc,pygame)
            self.temp.draw(self.screen)

            #self.player.rect.x += 10

        self.clock.tick(FPS)        #update screen at 60fps
        pygame.display.update()     #updates screen

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def collision_detect(self,player,entity_group):
        return pygame.sprite.spritecollide(player,entity_group,False)

    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()