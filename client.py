from _typeshed import Self
import pygame
from pygame.constants import K_DOWN, K_UP
from network import Network
from renderer import MyScreen

class MyGame():
    def __init__(self) -> None:
        pass

    def main(self):
        my_screen = MyScreen()
        # initiate the network and say hello to the server
        n = Network()
        new_data = n.receive()
        recv_msg_id = new_data["msg_id"]
        my_id = new_data["player_id"]
        send_msg_id = 1
        send_msg = {
            "send_msg_id" : send_msg_id,
            "msg" : "setup",
            "player_id" : my_id
        }
        n.send(send_msg)
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            new_data = n.receive()
            if new_data["msg_id"] > recv_msg_id:
                recv_msg_id = new_data["msg_id"]
                if new_data["msg"] == "playing":
                    my_screen.redraw_window(new_data, my_id)
            send_msg_id += 1
            send_data = self.get_send_data(my_id, send_msg_id)
            n.send(send_data)

    def get_send_data(self, my_id, msg_id):
        key_data = []
        keys = pygame.key.get_pressed()
        if keys == K_UP:
            key_data.append('up')
        elif keys == K_DOWN:
            key_data.append('down')
        data_to_send = {
            "msg_id" : msg_id,
            "player_id" : my_id,
            "key_data" : key_data
        }
        return data_to_send

if __name__ == '__main__':
    my_game = MyGame()
    my_game.main()