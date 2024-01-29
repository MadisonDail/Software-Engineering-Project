# Initialization from official documentation of the pygame library: https://www.pygame.org/docs/

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
pygame.freetype.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

# Set up buttons for the menu
screenWidth, screenHeight = pygame.display.get_window_size()
print(screenWidth)
print(screenHeight)
startButton = pygame.Rect(((screenWidth / 4), 300, (screenWidth / 2), 100))


running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(str(x) + " " + str(y))

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen, (0, 0 , 0), startButton)


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()