# check I still need all functions / methods

import pygame
import pong_constants as pc

class MyScreen:
    def __init__(self):
        self.win = pygame.display.set_mode((pc.WIDTH, pc.HEIGHT))
        pygame.display.set_caption("Online Pong")
        self.bat_image = self.make_bat()
        self.ball_image = self.make_ball()

    def redraw_window(self, new_data, my_id): # needs check for json data parsing
        self.win.fill((0, 0, 0))
        if new_data != {}:
            for obj in new_data:
                if obj == 'ball':
                    self.win.blit(self.ball_image, new_data[obj])
                elif obj == my_id:
                    pos = (10, new_data[obj])
                    self.win.blit(self.ball_image, pos)
                elif isinstance(obj, int):
                    pos = (470, new_data[obj])
                    self.win.blit(self.ball_image, pos)
        pygame.display.flip()

    def make_bat(self):
        image = pygame.Surface((20, 50))
        image.fill(pc.WHITE)
        return image
    
    def make_ball(self):
        image = pygame.Surface((20, 20))
        pygame.draw.circle(image, pc.WHITE, (10,10), 10)
        return image