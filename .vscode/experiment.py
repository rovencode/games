from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()

tile_a = 0
tile_b = 2

tile_x_layer = []

tile_map = [

]

for i in range(100):
    for j in range(100):
        tile_picker = randint(0, 2)

        if tile_picker == tile_a or tile_picker == tile_a + 1:
            tile_x_layer.append(tile_a)

        elif tile_picker == tile_b:
            tile_x_layer.append(tile_b)

    tile_map.append(tile_x_layer)
    tile_x_layer = []

for i in range(100):
    for j in range(100):
        if tile_map[i][j] == tile_a:
            Entity(model='cube', position=(i, 0, j), color=color.white, collider='box')
        elif tile_map[i][j] == tile_b:
            Entity(model='cube', position=(i, 0, j), color=color.white, collider='box')
            Entity(model='cube', position=(i, 1, j), color=color.black, scale=(1, 3, 1), collider='box')

player = FirstPersonController()

app.run()