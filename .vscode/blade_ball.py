from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

game = Ursina()
sky = Sky()

ground = Entity(
    model = 'plane',
    scale = (100, 1, 100),
    texture = 'white_cube',
    texture_scale = (100, 100),
    collider = 'box'
)
enemy = Button(
    parent = scene,
    model = 'sphere',
    color = color.red,
    scale = (2, 2, 2),
    position = (5, 1, 5),
    collider = 'sphere'
)
p2 = Entity(
    model = 'cube',
    color = color.blue,
    scale = (1, 2, 1),
    position = (5, 1, 5),
    collider = 'box'
)
p3 = Entity(
    model = 'cube',
    color = color.lime,
    scale = (1, 2, 1),
    position = (20, 1, 15),
    collider = 'box'
)
p4 = Entity(
    model = 'cube',
    color = color.yellow,
    scale = (1, 2, 1),
    position = (35, 1, 5),
    collider = 'box'
)
player = FirstPersonController()
ball_dir = player
ball_speed = 1
def update():
    global ball_speed
    global ball_dir
    if abs(enemy.x - ball_dir.x) < 3 and abs(enemy.z - ball_dir.z) < 3:
        if ball_dir == player:
            if mouse.left:
                ball_speed += 0.2
                rand_dir = randint(1, 3)
                if rand_dir == 1:
                    ball_dir = p2
                if rand_dir == 2:
                    ball_dir = p3
                if rand_dir == 3:
                    ball_dir = p4
        else:
            enemy.color = color.red
            ball_speed += 0.2
            rand_dir = randint(1, 4)
            if rand_dir == 1:
                ball_dir = player
            if rand_dir == 2:
                ball_dir = p2
            if rand_dir == 3:
                ball_dir = p3
            if rand_dir == 4:
                ball_dir = p4
    else:
        enemy.color = color.red

    if enemy.x > ball_dir.x:
        enemy.x -= ball_speed * time.dt
    if enemy.x < ball_dir.x:
        enemy.x += ball_speed * time.dt
    if enemy.z > ball_dir.z:
        enemy.z -= ball_speed * time.dt
    if enemy.z < ball_dir.z:
        enemy.z += ball_speed * time.dt

    if ball_dir.x > enemy.x and ball_dir is not player:
        ball_dir.x -= 2.5 * time.dt
    if ball_dir.x < enemy.x and ball_dir is not player:
        ball_dir.x += 2.5 * time.dt
    if ball_dir.z > enemy.z and ball_dir is not player:
        ball_dir.z -= 2.5 * time.dt
    if ball_dir.z < enemy.z and ball_dir is not player:
        ball_dir.z += 2.5 * time.dt
    
    if ball_speed > 30:
        ball_speed = 30
    
    if ball_dir == player:
        enemy.color = color.green

    if abs(enemy.x-player.x) < 0.5 and abs(enemy.z-player.z) < 0.5 and ball_dir == player:
        player.position = (0, 1, 0)
        enemy.position = (5, 1, 5)
        ball_speed = 1
        ball_dir = player
        p2.position = (5, 1, 5)
        p3.position = (20, 1, 15)
        p4.position = (35, 1, 5)
        p2.enable()
        p3.enable()
        p4.enable()

    if ball_dir == p2 and abs(enemy.x-p2.x) < 2 and abs(enemy.z-p2.z) < 2:
        death_chance = randint (1, 6)
        if death_chance == 1:
            p2.disable()
        else:
            pass
    if ball_dir == p3 and abs(enemy.x-p3.x) < 2 and abs(enemy.z-p3.z) < 2:
        death_chance = randint (1, 6)
        if death_chance == 1:
            p3.disable()
        else:
            pass
    if ball_dir == p4 and abs(enemy.x-p4.x) < 2 and abs(enemy.z-p4.z) < 2:
        death_chance = randint (1, 6)
        if death_chance == 1:
            p4.disable()
        else:
            pass
    if not p2.enabled and not p3.enabled and not p4.enabled:
        player.position = (0, 1, 0)
        enemy.position = (5, 1, 5)
        ball_speed = 1
        ball_dir = player
        p2.position = (5, 1, 5)
        p3.position = (20, 1, 15)
        p4.position = (35, 1, 5)
        p2.enable()
        p3.enable()
        p4.enable()
      
game.run()