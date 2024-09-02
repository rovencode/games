from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

game = Ursina()
sky = Sky()
inventory_block_positions = []
inventory_block_positions.append(0.2)
inventory_block_positions.append(0)
inventory_block_positions.append(0.1)

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
                self.tree_color = color.brown
        elif tree_type == 2:
                self.tree_color = color.white
        super().__init__(
            model = 'cube',
            color = self.tree_color,
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
    def mine_wood(self):
        global wood_plank_normal
        global tree_color
        if self.hovered and mouse.left and pickaxe_ == True:
            destroy(self)
            if self.tree_color == color.brown:
                wood_ore.enable()
                wood_plank_normal = 1
            elif self.tree_color == color.white:
                birch_ore.enable()

class Mountain(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model='sphere',
            color=color.gray,
            scale=(25, 100, 25),
            position=position,
        )

class Ore(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model = 'cube',
            color = color.gray,
            scale = (1, 10, 1),
            position = position,
            collider = 'box'
        )
    def mine(self):
        global ores_
        if self.hovered and mouse.left and pickaxe_ == True:
            cobble_ore.enable()
            destroy(self)

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
cobble_ore = Button(
            model = 'quad',
            color = color.gray,
            scale = (0.1, 0.1, 0.1),
            position = (inventory_block_positions[0],-0.4,0),
            texture = 'download__22_-removebg-preview (1)'
        )
wood_ore = Button(
    model = 'quad',
    color = color.brown,
    scale = (0.1, 0.1, 0.1),
    position = (inventory_block_positions[1],-0.4,0),
    texture = 'download (23)'
)
birch_ore = Button(
    model = 'quad',
    color = color.gray,
    scale = (0.1, 0.1, 0.1),
    position = (inventory_block_positions[2],-0.4,0),
    texture = 'download (24)'
)
class wood_block(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = 'cube',
            color = color.brown,
            scale = (1, 1, 1),
            position = position,
            collider = 'box'
        )

Ores = []
trees = []
for i in range(1050):
    trees.append(Tree(position = (randint(-1000, 1000), 0, randint(-1000, 1000))))
for i in range(50):
    mountain_x = randint(-1000, 1000)
    mountain_z = randint(-1000, 1000)
    Mountain(position = (mountain_x, 1, mountain_z))
    Ores.append(Ore(position = (mountain_x, 1, mountain_z)))
for i in range(20):
    House(position = (randint(-1000, 1000), 0, randint(-1000, 1000)))

inventory(position = (0, -0.4, 0))
print(inventory_block_positions)
wood_plank_normal = 0
pickaxe_ = False
def update():
    global wood_plank_normal
    global pickaxe_
    global ores_
    wood__ = False
    birch__ = False
    cobble__ = False
    if pickaxe_ == False:
        pickaxe.disable()
    if pickaxe_ == True:
        pickaxe.enable()
    if held_keys['1']:
          pickaxe_ = True
    if held_keys['2']:
          pickaxe_ = False

    if held_keys['3']:
        cobble__ = True
    if held_keys['4']:
        cobble__ = False

    if held_keys['5']:
        wood__ = True
        print("hi")
    if held_keys['6']:
        wood__ = False

    if held_keys['7']:
        birch__ = True
    if held_keys['8']:
        birch__ = False

    for ore in Ores:
        ore.mine()
    for tree in trees:
        tree.mine_wood()

    mouse_position = mouse.world_point
    if mouse.right and wood__ == True and wood_plank_normal == 1:
        wood_block(position = (mouse_position.x, mouse_position.y, mouse_position.z))


player = FirstPersonController(velocity = (0, 0, 0), speed = 12)
        
game.run()