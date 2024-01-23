import arcade


class Entity:
    def __init__(self,id,x,y):
        self.id = id                    #id to identify entity
        self.center_x = x                #x and y coords relative to map layout
        self.center_y = y

# class Player(Entity, arcade.AnimatedTimeBasedSprite):
    # def __init__(self,id,x,y,img,scale):
    #     Entity.__init__(self,id,x,y)   #inherit Entity class
    #     arcade.AnimatedTimeBasedSprite(img,scale)

class Player(arcade.AnimatedTimeBasedSprite):
    def update(self):
        self.movement_speed = 5
        self.center_x += self.change_x
        self.center_y += self.change_y

class NPC(arcade.AnimatedTimeBasedSprite):
    def update(self):
        self.movement_speed = 5
        self.center_x += self.change_x
        self.center_y += self.change_y