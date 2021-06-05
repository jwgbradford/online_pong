import pygame

class Player():
    def __init__(self):
        self.y = 230
        self.vel = 3

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.pos = (self.x, self.y)