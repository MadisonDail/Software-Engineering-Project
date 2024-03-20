# Initialization from official documentation of the pygame library: https://www.pygame.org/docs/

# Example file showing a basic pygame "game loop"
import pygame
import sys

#Defines the Class for New Game, handles all semantics New Game Screem will have
class NewGameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.fsu_garnet_color = (120, 47, 64)
        self.fsu_gold = (206, 184, 136)
        self.black = (0, 0, 0)  # Black color for the input box outline
        self.font = pygame.font.Font('Adobe Garamond Pro Regular.ttf', 35)
        self.game_name = ""  # The name entered by the user, this will be saved later 
        self.input_box = pygame.Rect(100, 250, 440, 50)  # Arbitrary input box dimensions
        self.active = False  # Input box is not active until clicked
        pygame.display.set_caption("New Game")

    def run(self):
        running = True
        while running:
            self.screen.fill(self.fsu_garnet_color)
            self.display_text("FLORIDA STATE POKEVERSITY", self.font, self.fsu_gold, 70, 70)
            # Display "Name of Game" above the input box
            self.display_text("Name of Game:", self.font, self.fsu_gold, 100, 200)
            # Render the current game name inside the input box
            pygame.draw.rect(self.screen, self.black, self.input_box, 2)  # outlines box in black
            self.display_text(self.game_name, self.font, self.fsu_gold, self.input_box.x+5, self.input_box.y+5)
            # Start Game Button
            start_game_btn = pygame.Rect(225, 350, 200, 50)  
            pygame.draw.rect(self.screen, self.fsu_garnet_color, start_game_btn)
            self.display_text("Start Game", self.font, self.fsu_gold, start_game_btn.x+30, start_game_btn.y+10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if self.input_box.collidepoint(event.pos):
                        self.active = not self.active
                    else:
                        self.active = False
                    # If the user clicked on the Start Game button.
                    if start_game_btn.collidepoint(event.pos):
                        print(f"Starting New Game: {self.game_name}")
                        # Will trnasition to new game 
                elif event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_BACKSPACE: #accounts for backspaces
                            self.game_name = self.game_name[:-1]
                        else:
                            self.game_name += event.unicode

            pygame.display.update()
        pygame.quit() 
        sys.exit()

    def display_text(self, txt, font, color, x, y):
        text_surf = font.render(txt, True, color)
        self.screen.blit(text_surf, (x, y))


class LoadScreen:
    def __init__(self, screen):
        self.screen = screen
        # Reuse some attributes from the MenuScreen
        self.fsu_garnet_color = (120, 47, 64)
        self.fsu_gold = (206, 184, 136)
        self.font = pygame.font.Font('Adobe Garamond Pro Regular.ttf', 35)
        # Three Saved Game Slots
        self.saved_games = ["Save 1     Game Name", "Save 2     Game Name", "Save 3     Game Name"]
        pygame.display.set_caption("Load Screen")

    def run(self):
        running = True
        while running:
            self.screen.fill(self.fsu_garnet_color)
            self.display_text("FLORIDA STATE POKEVERSITY", self.font, self.fsu_gold, 70, 70)
            # Display saved game slots
            for i, save in enumerate(self.saved_games):
                self.display_text(save, self.font, self.fsu_gold, 100, 150 + i * 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #if you click the x in corner 
                    running = False

            pygame.display.update()
        pygame.quit()
        sys.exit()

    def display_text(self, txt, font, color, x, y):
        text = font.render(txt, True, color)
        self.screen.blit(text, (x, y))


class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.fsu_garnet_color = (120, 47, 64)  # color for fsu garnet
        self.fsu_gold = (206, 184, 136)  # fsu gold for font
        self.font = pygame.font.Font('Adobe Garamond Pro Regular.ttf', 35)

        # Button information
        self.buttons = {
            "NEW GAME": {"x": 225, "y": 150, "width": 200, "height": 50},
            "LOAD GAME": {"x": 225, "y": 225, "width": 200, "height": 50},
            "QUIT GAME": {"x": 225, "y": 300, "width": 200, "height": 50}
        }

    def run(self):
        running = True
        while running:
            self.screen.fill(self.fsu_garnet_color)  # FSU Garnet background
            self.display_text("FLORIDA STATE POKEVERSITY", self.font, self.fsu_gold, 70, 70)
            for text, info in self.buttons.items():
                self.display_button(text, info["x"], info["y"], info["width"], info["height"], self.fsu_garnet_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # checks if buttons have been clicked
                    for action, info in self.buttons.items():
                        if info["x"] <= mouse_x <= info["x"] + info["width"] and info["y"] <= mouse_y <= info["y"] + info["height"]:
                            print(f"{action} CLICKED!")
                            if action == "QUIT GAME":
                                running = False # exits the menu screen loop 
                            elif action == "LOAD GAME":
                                load_screen = LoadScreen(self.screen)
                                load_screen.run()
                                running = False  # Exit the menu screen loop
                            elif action == "NEW GAME":
                                new_game_screen = NewGameScreen(self.screen)
                                new_game_screen.run()
                                running = False  # Exit the menu screen loop

            pygame.display.update()
        pygame.quit()
        sys.exit()

    def display_text(self, txt, font, color, x, y):
        text = font.render(txt, True, color)
        self.screen.blit(text, (x, y))

    def display_button(self, text, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        text_width, text_height = self.font.size(text)
        x_center = x + (width - text_width) / 2
        y_center = y + (height - text_height) / 2
        self.display_text(text, self.font, self.fsu_gold, x_center, y_center)

# Pygame setup
pygame.init()
WIN_WIDTH, WIN_HEIGHT = 640, 480
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Menu Screen")

# Run the menu screen
menu_screen = MenuScreen(screen)
menu_screen.run()
