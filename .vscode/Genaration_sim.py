from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

game = Ursina()
sky = Sky()

ground = Entity(
    model = 'plane',
    scale = (1000, 1, 1000),
    texture = 'grass',
    texture_scale = (100, 100),
    collider = 'box'
)
pickaxe = Button(
    model = 'quad',
    color = color.brown,
    scale = (1, 2, 1),
    position = (-0.8, -0.4, 0),
    texture = 'download__26_-removebg-preview'
)


class Tree(Entity):
    def __init__(self, position = (0, 0, 0,)):
        tree_height = randint(5,10)
        tree_width = tree_height / 10
        tree_type = randint(1,2)
        if tree_type == 1:
                tree_color = color.brown
        elif tree_type == 2:
                tree_color = color.white
        super().__init__(
            model = 'cube',
            color = tree_color,
            scale = (1, randint(7,10), 1),
            position = position,
            collider = 'box'
        )
        self.leaves = Entity(
            parent = self,
            model = 'sphere',
            color = color.green,
            scale = (tree_height, tree_width, tree_height),
            position = (0, tree_height/100 * 10, 0)
        )
class Mountain(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model='sphere',
            color=color.gray,
            scale=(25, 100, 25),
            position=position,
        )
    def generate_ore(self):
        self.ore = Entity(
            model = 'cube',
            color = color.dark_gray,
            scale = (1, 10, 1),
            position = (0, 0, 0),
            collider = 'box'
        )

class House(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model = 'cube',
            color = color.gray,
            scale = (10, 15, 10),
            position = position,
        )
        self.roof_p1 = Entity(
            parent = self,
            model = 'cube',
            color = color.brown,
            scale = (1.5, 0.20, 1.5),
            position = (0, 0.5, 0)
        )
        self.roof_p2 = Entity(
            parent = self,
            model = 'cube',
            color = color.brown,
            scale = (1, 0.20, 1),
            position = (0, 0.70, 0)
        )
        self.door = Entity(
            parent = self,
            model = 'cube',
            color = color.black,
            scale = (0.2, 0.2, 0.1),
            position = (0, 0.1, 0.5)
        )
class inventory(Button):
     def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model = 'quad',
            color = color.white,
            scale = (0.50, 0.1, 0.1),
            position = position,
          )
        self.pickaxe = Button(
            parent = self,
            model = 'quad',
            color = color.brown,
            scale = (0.3, 0.5, 0.3),
            position = (-0.30, 0, 0),
            texture = 'download__26_-removebg-preview'
        )
      
trees = []
mountains = []
houses = []
for i in range(1050):
    tree = Tree(position = (randint(-1000, 1000), 0, randint(-1000, 1000)))
    trees.append(tree)
for i in range(50):
    mountain = Mountain(position = (randint(-1000, 1000), 1, randint(-1000, 1000)))
    mountains.append(mountain)
    for mountain in mountains:
        mountain.generate_ore()
for i in range(20):
    house = House(position = (randint(-1000, 1000), 0, randint(-1000, 1000)))
    houses.append(house)

inventory(position = (0, -0.4, 0))

pickaxe_ = False
def update():
    global pickaxe_
    if pickaxe_ == False:
        pickaxe.disable()
    if pickaxe_ == True:
        pickaxe.enable()
    if held_keys['1']:
          pickaxe_ = True
    if held_keys['2']:
          pickaxe_ = False
    for mountain in mountains:
        if mountain.ore.hovered and pickaxe_ == True:
            mountain.ore.disable()
    



player = FirstPersonController()
        
game.run()