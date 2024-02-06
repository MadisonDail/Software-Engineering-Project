import pygame
import entity   #import classes from entity.py

def check_collision(s1,s2,spriteList):
    ifCollision = pygame.sprite.collide_rect(s1,s2)
    if ifCollision:                 #if first and second sprite rect collided, remove second sprite
        spriteList.remove(s2)

pygame.init()
width = 800
height = 800
window_size = (width,height)
screen = pygame.display.set_mode(window_size)

sprites = pygame.sprite.Group()
player_image = "images/player_stand.png"
trainerNPC_image = "images/player_stand.png"

player_sprite = entity.Player("player",400,400,player_image,screen)
trainerNPC_sprite = entity.TrainerNPC("bug",500,500,trainerNPC_image,screen)
sprites.add(player_sprite)
sprites.add(trainerNPC_sprite)

clock = pygame.time.Clock()         #get clock
running = True
while running:
    screen.fill((0,0,0))             #call fill to remove movement duplicates
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    check_collision(player_sprite,trainerNPC_sprite,sprites)
    sprites.update()            #update all sprites in group
    sprites.draw(screen)        #draw sprites to screen
    pygame.display.flip()       #update the display   
    clock.tick(30)              #run at 30 fps to avoid possible program issues        


pygame.quit()
