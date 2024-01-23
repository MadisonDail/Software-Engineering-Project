import arcade
from entity import Player
from entity import Entity

class Pokeversity(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        
        self.set_location(200,200)
        self.player_list = None
        self.player_sprite = None
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        player_image = "images/player_stand.png"


        self.player_sprite = Player(player_image,0.05)  #Player object from entity.py, 0.05 is scaling of image
        self.player_sprite.center_x = self.width//2
        self.player_sprite.center_y = self.height//2
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()
    
    def on_key_press(self,key,modifiers):       #will change to smoother key_press soon
        if key == arcade.key.UP:
            self.player_sprite.change_y = self.player_sprite.movement_speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -self.player_sprite.movement_speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = self.player_sprite.movement_speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -self.player_sprite.movement_speed

    def on_key_release(self,key,modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player_sprite.change_x = 0

def main():
    window = Pokeversity(720,720,'Florida State Pokeversity')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
