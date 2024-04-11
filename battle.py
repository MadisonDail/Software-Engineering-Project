import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Load the Pokémon images
player_pokemon_image = pygame.image.load('images/pokemon/oshawott.png').convert_alpha()
opponent_pokemon_image = pygame.image.load('images/pokemon/pika_battle.webp').convert_alpha()

font = pygame.font.Font('Adobe Garamond Pro Regular.ttf', 35)

#  text surfaces
player_poke = font.render("Pokemon", True, (0, 0, 0))
poke_name = font.render("Pokemon 2", True, (0, 0, 0))
run = font.render("Run", True, (0, 0, 0))
ball = font.render("Ball", True, (0, 0, 0))
fight = font.render("Fight", True, (0, 0, 0))
pokemon = font.render("Pokémon", True, (0, 0, 0))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #need to add player clicks and stuff 
 
    screen.fill((255, 255, 255))  

    # Draw Pokémon images
    screen.blit(player_pokemon_image, (50, 100))  
    screen.blit(opponent_pokemon_image, (400, 50))  

    # Draw text surfaces
    screen.blit(player_poke, (50, 50))  
    screen.blit(poke_name, (400, 10)) 
    screen.blit(run, (50, 350))  
    screen.blit(ball, (150, 350))  
    screen.blit(fight, (250, 350))  
    screen.blit(pokemon, (350, 350))  
    # Update display
    pygame.display.flip()

pygame.quit()
