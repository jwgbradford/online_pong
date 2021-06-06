import pygame
from network import Network
from renderer import MyScreen

def main():
    my_screen = MyScreen()
    run = True
    n = Network()
    my_id = n.receive()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys = pygame.key.get_pressed()
        n.send(keys)
        new_data = n.receive()
        my_screen.redraw_window(new_data, my_id)

main()