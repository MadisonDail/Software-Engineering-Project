import pygame
import pokemon

def BattleScreen(userP, enemyP, userPokemonIndex, enemyPokemonIndex, switchFlag):
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    # Load the Pokémon images
    player_pokemon_image = pygame.image.load("images/pokemon/" + userP[userPokemonIndex].name + ".png").convert_alpha()
    opponent_pokemon_image = pygame.image.load("images/pokemon/" + enemyP[enemyPokemonIndex].name + ".png").convert_alpha()

    font = pygame.font.Font('Adobe Garamond Pro Regular.ttf', 35)
    fsu_gold = (206, 184, 136)
    fsu_red = (120, 47, 64)
    buttons = [
        pygame.Rect(150, 300, 100, 50),
        pygame.Rect(400, 300, 100, 50),
        pygame.Rect(150, 350, 100, 50),
        pygame.Rect(400, 350, 100, 50)
    ]

    button_text= ["Run", "Catch", "Fight", "Pokémon"]

    fight_buttons = [
        pygame.Rect(150, 300, 100, 50),
        pygame.Rect(400, 300, 100, 50),
        pygame.Rect(150, 350, 100, 50),
        pygame.Rect(400, 350, 100, 50)
    ]

    fight_text=[userP[userPokemonIndex].move1.name,
                userP[userPokemonIndex].move2.name,
                userP[userPokemonIndex].move3.name,
                userP[userPokemonIndex].move4.name 
    ]
    # fight_text=["Move 1", "Move 2", "Move 3", "Move 4"]
    
    

    pokemon_text = []
    for poke in userP:
        pokemon_text.append(poke.name)
    pokemon_buttons = [
        pygame.Rect(150, 300, 100, 50),
        pygame.Rect(400, 300, 100, 50),
        pygame.Rect(150, 350, 100, 50),
        pygame.Rect(400, 350, 100, 50),
        pygame.Rect(150, 400, 100, 50),
        pygame.Rect(400, 400, 100, 50)
    ]

    def display_text(txt, font, color, x, y):
        text = font.render(txt, True, color)
        screen.blit(text, (x, y))

    # Update display
    # Main game loop

    #updates display, determines what is inside the text
    fight_options= False
    pokemon_options = False
    current_buttons = buttons
    current_text = button_text


    running = True
    if(not switchFlag):
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit() #should exit the game if you click x, gives error for now but it exits the screen at least lol
                    # sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, index in zip(current_buttons, current_text):
                        if rect.collidepoint(event.pos):
                            if fight_options:
                                if index==index:
                                    move = index
                                    running=False
                                    return "MOVE " + move
                                    # break   
                                    # fight_options=False
                                    # current_buttons = buttons
                                    # current_text = button_text
                            elif pokemon_options:
                                if index==index:
                                    pokemon = index
                                    running = False
                                    return "POKEMON " + pokemon
                            else:
                                if index=="Fight": #fight index
                                    fight_options = True
                                    current_buttons = fight_buttons
                                    current_text=fight_text
                                if index=="Run":
                                    pygame.quit()  #doesnt work but quits so fine for rn 
                                if index=="Pokémon":
                                    pokemon_options = True
                                    current_buttons = pokemon_buttons
                                    current_text=pokemon_text
                                if index=="Catch":
                                    return "CATCH"
                                else:
                                    print(index)
            screen.fill((120, 47, 64)) 
 

            # Draw Pokémon images
            screen.blit(player_pokemon_image, (100, 145))  
            screen.blit(opponent_pokemon_image, (350, 145))  

            # Draw text surfaces
            display_text(str(userP[userPokemonIndex].name), font, fsu_gold, 100, 50)
            display_text(str(enemyP[enemyPokemonIndex].name), font, fsu_gold, 400, 50)
            display_text("HP " + str(userP[userPokemonIndex].currentHp), font, fsu_gold, 110, 100)
            display_text("HP " + str(enemyP[enemyPokemonIndex].currentHp) , font, fsu_gold, 400, 100)
            
            for button, text in zip(current_buttons, current_text):
                pygame.draw.rect(screen, fsu_red, button)
                displaytext= font.render(text, True, fsu_gold)
                screen.blit(displaytext, (button.x, button.y))

            pygame.display.flip()
    else:
        print("SWITCHING POKEMON")
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit() #should exit the game if you click x, gives error for now but it exits the screen at least lol
                    # sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, index in zip(current_buttons, current_text):
                        if rect.collidepoint(event.pos):
                            if pokemon_options:
                                if index==index:
                                    pokemon = index
                                    running = False
                                    return "POKEMON " + pokemon
            screen.fill((120, 47, 64))  

            # Draw Pokémon images
            screen.blit(player_pokemon_image, (100, 145))  
            screen.blit(opponent_pokemon_image, (350, 145))  

            # Draw text surfaces
            display_text(str(userP[userPokemonIndex].name), font, fsu_gold, 100, 50)
            display_text(str(enemyP[enemyPokemonIndex].name), font, fsu_gold, 400, 50)
            display_text("HP " + str(userP[userPokemonIndex].currentHp), font, fsu_gold, 110, 100)
            display_text("HP " + str(enemyP[enemyPokemonIndex].currentHp) , font, fsu_gold, 400, 100)
            
            for button, text in zip(current_buttons, current_text):
                pygame.draw.rect(screen, fsu_red, button)
                displaytext= font.render(text, True, fsu_gold)
                screen.blit(displaytext, (button.x, button.y))

            pygame.display.flip()
    

        pygame.quit()
# BattleScreen()