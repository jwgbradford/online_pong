# check I still need all functions / methods

import pygame
import pong_constants as pc

class MyScreen:
    def __init__(self):
        width = 500
        height = 500
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Online Pong")
        self.game_objects = self.add_objects(width, height)

    def redraw_window(self):
        for obj in self.game_objects:
            screen_object = self.game_objects[obj]
            self.win.blit(screen_object['image'], screen_object['pos'])
        pygame.display.flip()

    def add_objects(self, w, h):
        game_objects = {}
        game_objects['ball'] = {'image' : self.make_ball, 'pos' : (w / 2, h / 2)}
        game_objects['p1'] = {'image' : self.make_bat, 'pos' : (10, h / 2)}
        game_objects['p2'] = {'image' : self.make_bat, 'pos' : (470, h / 2)}
        return game_objects

    def make_bat(self):
        image = pygame.Surface((20, 50))
        image.fill(pc.WHITE)
        return image
    
    def make_ball(self):
        image = pygame.Surface((20, 20))
        pygame.draw.circle(image, pc.WHITE, (10,10), 10)
        return image