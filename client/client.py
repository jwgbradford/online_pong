import pygame
from network import Network
from renderer import MyScreen

class MyGame():
    def __init__(self) -> None:
        pass

    def main(self):
        # initiate the network and say hello to the server
        n = Network()
        new_data = n.receive()

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

    def set_up_game(self, data):
        recv_msg_id = data["msg_id"]
        my_id = data["player_id"]
        width = data["data"]["width"]
        height = sata["data"]["height"]
        my_screen = MyScreen((width, height))
        send_msg_id = 1
        send_msg = {
            "send_msg_id" : send_msg_id,
            "msg" : "setup",
            "player_id" : my_id
        }
        
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
            "data" : key_data
        }
        return data_to_send

if __name__ == '__main__':
    my_game = MyGame()
    my_game.main()