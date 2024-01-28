import pygame
import entity   #import classes from entity.py

pygame.init()
width = 800
height = 800
window_size = (width,height)
screen = pygame.display.set_mode(window_size)

sprites = pygame.sprite.Group()
player_image = "images/player_stand.png"

player_sprite = entity.Player("player",400,400,player_image)
player_sprite.show_hitbox(screen)
sprites.add(player_sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        sprites.update()            #update all sprites in group
        sprites.draw(screen)        #draw sprites to screen
        pygame.display.flip()       #update the display   


pygame.quit()
