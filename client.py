import pygame
from network import Network
import pong_constants as pc

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Online Pong")

def redrawWindow(win, bat, player, player2):
    win.fill((0, 0, 0))
    win.blit(bat, player.pos)
    win.blit(bat, player2.pos)
    pygame.display.flip()

def make_bat():
    image = pygame.Surface((20, 50))
    image.fill(pc.WHITE)
    return image

def main():
    run = True
    n = Network()
    p = n.getP()
    p.x = 10
    p.update()
    
    clock = pygame.time.Clock()
    bat = make_bat()

    while run:
        clock.tick(60)

        p2 = n.send(p)
        p2.x = 470
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, bat, p, p2)

main()