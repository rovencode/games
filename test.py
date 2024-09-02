from pygamejr import game
import random
import numpy as np

game.start("Roven's Game", 1024, 768, "purple")

player = game.create_rect(50, 50, 1024/2, 768/2, color='red')

enemies = []
for i in range(3):
    enemy = game.create_ellipse(50, 50, random.randint(0, 1024), random.randint(0, 768), color='blue')
    enemies.append(enemy)

enemy_speed = 1.6
player_speed = 2

def player_keyboard(player, keys):
    if "left" in keys:
        player.move(-player_speed, 0)
    elif "right" in keys:
        player.move(player_speed, 0)
    elif "up" in keys:
        player.move(0, -player_speed)
    elif "down" in keys:
        player.move(0, player_speed)
game.handle(player.on_keypress, player_keyboard)

def glide_player(enemy):
    player_x, player_y = player.rect().x, player.rect().y
    enemy_x, enemy_y = enemy.rect().x, enemy.rect().y
    dx, dy = player_x-enemy_x, player_y-enemy_y
    mag = np.sqrt(dx**2 + dy**2)
    if mag == 0:
        return
    dx, dy = dx/mag, dy/mag
    dx, dy = dx * enemy_speed, dy*enemy_speed*enemy_speed
    enemy.move(dx, dy)

while game.running:
    for enemy in enemies:
        glide_player(enemy)

    for enemy in enemies:
        if player.touches(enemy):
            print("Game Over!")
            game.end()

    game.update()