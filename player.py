from entity import *
import pygame

class Player(Entity):                       #inherit from entity
    def __init__(self,id,game,layer,x,y,spriteImage,screen):
        super().__init__(id,game,layer,x,y,spriteImage,screen)

    def movement(self):                     
    # adjust sprite position if a key is pressed
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            new_rect = self.rect.move(-self.velocity, 0) #if a collision, it will not move
            if not self.tile_collision(new_rect.x // TILE_SIZE, self.rect.y // TILE_SIZE):
                self.rect = new_rect # if collision gets updated
        if key_press[pygame.K_RIGHT]:
            new_rect = self.rect.move(self.velocity, 0)
            if not self.tile_collision(new_rect.x // TILE_SIZE, self.rect.y // TILE_SIZE):
                self.rect = new_rect
        if key_press[pygame.K_UP]:
            new_rect = self.rect.move(0, -self.velocity)
            if not self.tile_collision(self.rect.x // TILE_SIZE, new_rect.y // TILE_SIZE):
                self.rect = new_rect
        if key_press[pygame.K_DOWN]:
            new_rect = self.rect.move(0, self.velocity)
            if not self.tile_collision(self.rect.x // TILE_SIZE, new_rect.y // TILE_SIZE):
                self.rect = new_rect
        current_x = self.rect.x // TILE_SIZE # updates x&y position 
        current_y = self.rect.y // TILE_SIZE

        if self.game.tilemap[current_y][current_x] == 'X':
            # Here you can choose which tilemap to switch to
            self.game.changeMap(tilemap)

        elif self.game.tilemap[current_y][current_x] == '0':
            self.game.changeMap(tilemap0)

        elif self.game.tilemap[current_y][current_x] == '1':
            self.game.changeMap(tilemap1)

        elif self.game.tilemap[current_y][current_x] == '2':
            self.game.changeMap(tilemap2)

        elif self.game.tilemap[current_y][current_x] == '3':
            self.game.changeMap(tilemap3)

    #accounts for what tiles you are on, changes accordingly        
    def tile_collision(self, x, y):
        # Check if the tile at the given (x, y) position is a 'B'
        if self.game.tilemap[y][x] == 'B':
            return True
        #checks to see if it is an "exit"
        else:
            return False

    def update(self):                       #check for key press for every update
        self.movement()

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        #block is square 32x32 pixels
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE 
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
        