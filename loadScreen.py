# Initialization from official documentation of the pygame library: https://www.pygame.org/docs/

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup

def DisplayLoad():
    pygame.init()
    pygame.freetype.init()
    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()

    # Set up buttons for the menu
    screenWidth, screenHeight = pygame.display.get_window_size()
    print(screenWidth)
    print(screenHeight)
    startButton = pygame.Rect(((screenWidth / 4), (screenHeight / 4), (screenWidth / 2), 100))
    # loadButton = pygame.Rect(((screenWidth / 4), (screenHeight / 4) * 2, (screenWidth / 2), 100))
    # quitButton = pygame.Rect(((screenWidth / 4), (screenHeight / 4) * 3, (screenWidth / 2), 100))

    # Initialize font
    font = pygame.font.Font('ProtestStrike-Regular.ttf', 84)

    # Create text
    # Note: needs updating
    startFont = font.render('  Game 1  ', True, (0, 0, 255), (100, 0, 0))
    # loadFont = font.render('   Load Game   ', True, (0, 0, 255), (100, 0, 0))
    # quitFont = font.render('   Quit Game    ', True, (0, 0, 255), (100, 0, 0))

    # Functions for checking to see if the coordinates of the click overlap a button
    # Will replace print statement once we get different screen views created
    def checkGameClicked(x, y):
        if(x > (screenWidth / 4) and x < ((screenWidth / 4) + (screenWidth / 2)) and y > screenHeight / 4 and y < (screenHeight / 4) + 100):
            return True

    # def checkLoadClicked(x, y):
    #     if(x > (screenWidth / 4) and x < ((screenWidth / 4) + (screenWidth / 2)) and y > ((screenHeight / 4) * 2) and y < (screenHeight / 4) * 2 + 100):
    #         print('load')

    # def checkQuitClicked(x, y):
    #     if(x > (screenWidth / 4) and x < ((screenWidth / 4) + (screenWidth / 2)) and y > ((screenHeight / 4) * 3) and y < (screenHeight / 4) * 3 + 100):
    #         print('quit')

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check coordinates of mouse click
                    x, y = pygame.mouse.get_pos()
                    print(str(x) + " " + str(y))
                    # if(checkGameClicked(x, y)):
                        # load map here 
                    # checkLoadClicked(x, y)
                    # checkQuitClicked(x, y)
                    

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("red")
        pygame.draw.rect(screen, (0, 0 , 0), startButton)
        # pygame.draw.rect(screen, (0, 0 , 0), loadButton)
        # pygame.draw.rect(screen, (0, 0 , 0), quitButton)
        # Display text after the buttons have been created
        screen.blit(startFont, startButton)
        # screen.blit(loadFont, loadButton)
        # screen.blit(quitFont, quitButton)

        # flip() the display to put your work on screen
        pygame.display.flip()
        pygame.display.update()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()