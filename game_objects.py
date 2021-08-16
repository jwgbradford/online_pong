import math
from pygame import K_UP, K_DOWN
from random import randint

class GameObject():
    def __init__(self, id) -> None:
        self.id = id
        self.vel = 3
        self.x, self.y = 0, 0

class Player(GameObject):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.x = self.set_x()

    def set_x(self):
        x = 230
        if self.id == 1:
            return x
        else:
            return -x

    def move(self, data):
        if data['move'] == 'up':
            print('go up')
            self.y -= self.vel
            if self.y < 5:
                self.y = 5
        if data['move'] == 'down':
            self.y += self.vel
            if self.y > 495:
                self.y = 495

    def update(self, data):
        self.move(data)
        pos = (self.x, self.y)
        return pos

class Ball(GameObject):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.y = 250
        self.x = 250
        self.dir = randint(45, 125) * (math.pi / 180)
        self.dx = self.vel * math.sin(self.dir)
        self.dy = self.vel * math.cos(self.dir)

    def check_bounce(self, game_data):
        if self.y < 5:
            self.dy *= -1
        elif self.y > 495:
            self.dy *= -1
        if self.bat_bounce(game_data):
            self.dx *= -1
            self.x += self.dx * 2

    def bat_bounce(self, game_data):
        if self.x >= 250: # check bounce player 2
            pass
        else: # check bounce player 1
            pass

    def move(self):
        self.y += self.dy
        self.x += self.dx

    def update(self):
        self.move()
        pos = (self.x, self.y)
        return pos