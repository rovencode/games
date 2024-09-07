from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import numpy as np

class FlyingController(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gravity = 0
        self.speed = 10

    def update(self):
        super().update()
        if held_keys['space']:
            self.y += self.speed * time.dt
        if held_keys['shift']:
            self.y -= self.speed * time.dt

app = Ursina()

# Generate cube positions
def generate_positions(num_cubes):
    side_length = int(np.ceil(np.cbrt(num_cubes)))
    positions = np.mgrid[0:side_length, 0:side_length, 0:side_length].reshape(3, -1).T * 2
    return positions[:num_cubes]

# Initialize instance data
num_cubes = 10000
positions = generate_positions(num_cubes)

# Create parent entity
parent = Entity()

# Create cubes as children of the parent entity
for pos in positions:
    Entity(model='cube', color=color.random_color(), position=Vec3(*pos), parent=parent)

# Create a FlyingController for navigation
player = FlyingController(y=5, origin_y=-.5)

# Create Text entity for FPS counter
fps_counter = Text(text='FPS: 0', position=(-.85, .45), color=color.yellow)

def update():
    # Update FPS counter
    fps_counter.text = f'FPS: {round(1/time.dt)}'  # time.dt is the delta time between frames

# Instructions text
instructions = Text(
    text='WASD to move, Space to fly up, Shift to fly down\nMouse to look around, Esc to exit',
    position=(-.85, -.45),
    color=color.light_gray,
    scale=0.7
)

# Run the app
app.run()