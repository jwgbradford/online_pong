import math
from pygame import K_UP, K_DOWN
from random import randint

class Player():
    def __init__(self, id):
        self.id = id
        self.y = 230
        self.x = 0 # we're not interested in the x value but need to pass something
        self.vel = 3
        self.pos = (self.x, self.y)

    def move(self, data):
        if data['move'] == 'up': # only works if passing pickles, we're passing json
            print('go up')
            self.y -= self.vel
            if self.y < 5:
                self.y = 5
        if data['move'] == 'down':
            self.y += self.vel
            if self.y > 495:
                self.y = 495
        self.update()

    def update(self):
        self.pos = (self.x, self.y)

class Ball():
    def __init__(self):
        self.id = 0
        self.y = 250
        self.x = 250
        self.vel = 3
        self.dir = randint(45, 125) * (math.pi / 180)
        self.dx = self.vel * math.sin(self.dir)
        self.dy = self.vel * math.cos(self.dir)

    def move(self):
        self.y += self.dy
        self.x += self.dx
        if self.x < 5:
            self.dx *= -1
        elif self.x > 495:
            self.x *= -1
        self.update()

    def update(self):
        self.pos = (self.x, self.y)