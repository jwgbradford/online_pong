import pygame
from network import Network
from renderer import MyScreen

def main():
    my_screen = MyScreen()
    run = True
    n = Network()

    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys = pygame.key.get_pressed()
        my_screen.game_objects = n.send(keys)
        if my_screen.game_objects:
            my_screen.redraw_window()
        clock.tick(60)

main()