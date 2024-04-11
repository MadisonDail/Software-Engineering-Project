import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

# Load the Pokémon images
player_pokemon_image = pygame.image.load('images/pokemon/oshawott.png').convert_alpha()
opponent_pokemon_image = pygame.image.load('images/pokemon/pikachu.png').convert_alpha()

font = pygame.font.Font('Adobe Garamond Pro Regular.ttf', 35)
fsu_gold = (206, 184, 136)

def display_text(txt, font, color, x, y):
        text = font.render(txt, True, color)
        screen.blit(text, (x, y))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #need to add player clicks and stuff 
 
    screen.fill((120, 47, 64))  

    # Draw Pokémon images
    screen.blit(player_pokemon_image, (100, 100))  
    screen.blit(opponent_pokemon_image, (350, 100))  

    # Draw text surfaces
    display_text("Oshawott", font, fsu_gold, 100, 50)
    display_text("Pikachu", font, fsu_gold, 400, 50)
    display_text("HP 87/87", font, fsu_gold, 100, 100)
    display_text("HP 87/87", font, fsu_gold, 400, 100)
    display_text("Run", font, fsu_gold, 150, 300)
    display_text("Ball", font, fsu_gold, 400 , 300)
    display_text("Fight", font, fsu_gold, 150, 350)
    display_text("Pokémon", font, fsu_gold, 400, 350) 
    # Update display
    pygame.display.flip()

pygame.quit()
