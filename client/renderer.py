# check I still need all functions / methods

import pygame

class MyScreen:
    def __init__(self, screen_size):
        self.win = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Online Pong")
        self.bat_image = self.make_bat()
        self.ball_image = self.make_ball()
        self.clock = pygame.time.Clock()

    def redraw_window(self, recv_data, my_id): # needs check for json data parsing
        self.win.fill((0, 0, 0))
        if my_id == 1:
            other_id = 2
            ball_x = recv_data[0]["pos_x"]
        else:
            other_id = 1
            ball_x = recv_data[0]["pos_x"] * -1
        ball_pos = (ball_x, recv_data[0]["pos_y"])
        self.win.blit(self.ball_image, ball_pos)
        my_pos = (10, recv_data[my_id]["pos_y"])
        self.win.blit(self.bat_image, my_pos)
        other_pos = (470, recv_data[other_id]["pos_y"])
        self.win.blit(self.bat_image, other_pos)
        self.clock.tick(60)
        pygame.display.flip()

    def make_bat(self):
        image = pygame.Surface((20, 50))
        image.fill(pc.WHITE)
        return image
    
    def make_ball(self):
        image = pygame.Surface((20, 20))
        pygame.draw.circle(image, pc.WHITE, (10,10), 10)
        return image