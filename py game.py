import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos_x,player_pos_y = screen.get_width()/2,screen.get_height()/2

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    pygame.draw.rect(screen, (255,0,0), (screen, player_pos_x,player_pos_y,40,40))
    pygame.display.update()