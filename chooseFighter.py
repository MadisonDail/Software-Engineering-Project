import pygame
import sys
import copy
import pokedex

# Initialize Pygame
def chooseStarter():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Select Pokemon")

    # Define colors and font
    fsu_garnet_color = (120, 47, 64)
    fsu_gold = (206, 184, 136)
    black = (0, 0, 0)
    font = pygame.font.Font('Adobe Garamond Pro Regular.ttf', 35)

    # Define the positions and sizes for the placeholders and text
    image_positions = [(50, 135), (250, 135), (450, 135)]
    text_positions = [(50, 300), (250, 300), (450, 300)]
    placeholder_size = (150, 150)  # Width and height of the placeholder rectangles

    # Define Pokémon names
    pokemon_names = ["Squirtle", "Bulbasaur", "Charmander"]

    # Load the Pokémon images
    pokemon_images = [
        pygame.image.load('images/pokemon/Squirtle.png').convert_alpha(),
        pygame.image.load('images/pokemon/Bulbasaur.png').convert_alpha(),
        pygame.image.load('images/pokemon/Charmander.png').convert_alpha()
    ]

    # Define buttons as Rects for text
    button_rects = [pygame.Rect(pos[0], pos[1] + 150, placeholder_size[0], 40) for pos in image_positions]

    # Main game loop
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, btn_rect in enumerate(button_rects):
                    if btn_rect.collidepoint(mouse_pos):
                        print(f"{pokemon_names[i]} button clicked!")
                        if(pokemon_names[i] == "Bulbasaur"):
                            return copy.copy(pokedex.Pokedex[0])
                        elif(pokemon_names[i] == "Charmander"):
                            return copy.copy(pokedex.Pokedex[3])
                        elif(pokemon_names[i] == "Squirtle"):
                            return copy.copy(pokedex.Pokedex[6])
                        return pokemon_names[i]

        # Fill the screen with the background color
        screen.fill(fsu_garnet_color)

        # Draw the Pokémon images and text for each Pokémon
        for i in range(3):
            # Scale the image to the placeholder size and draw it
            screen.blit(pokemon_images[i], image_positions[i])

            # Draw the button rectangles
            button_rect = button_rects[i]
            pygame.draw.rect(screen,fsu_garnet_color , button_rect)
            
            # Draw the text label inside the button rectangles
            pokemon_text_surface = font.render(pokemon_names[i], True, fsu_gold)
            text_rect = pokemon_text_surface.get_rect(center=button_rect.center)
            screen.blit(pokemon_text_surface, text_rect)

        # Update the display
        pygame.display.flip()
    pygame.quit()