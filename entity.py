import arcade


class Entity(arcade.AnimatedTimeBasedSprite):
    def __init__(self,id,x,y,filename,scale=0.05):
        super().__init__(filename,scale)
        self.id = id                        #id to identify entity
        self.center_x = x                   #x and y coords relative to map layout
        self.center_y = y
    
    def update(self):
        super().update()

    def draw(self):
        super().draw()


class Player(Entity):
    def __init__(self,id,x,y,filename,scale=0.05):
        super().__init__(id,x,y,filename,scale)

    def update(self):
        super().update()
        self.movement_speed = 3
        self.center_x += self.change_x
        self.center_y += self.change_y

class NPC(arcade.AnimatedTimeBasedSprite):
    def update(self):
        self.movement_speed = 0
        self.center_x += self.change_x
        self.center_y += self.change_y