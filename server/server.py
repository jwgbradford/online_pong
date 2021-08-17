import socket, json, time
from threading import Thread
from game_objects import Player, Ball
import pong_constants as pc

class PongServer():
    def __init__(self) -> None:
        self.game_objects = []
        self.output_buffer = {}
        self.input_buffer = {}

    def run(self):
        self.start_server()
        pong_engine = Thread(target=self.threaded_engine, args=())
        pong_engine.start()
        player_number = 1
        while True:
            print("Waiting for client, Pong Engine Started")
            conn, addr = self.server_socket.accept()
            print("Connected to:", addr[1])
            connected_player = Thread(target=self.threaded_player, args=(conn, player_number))
            connected_player.start()
            player_number += 1

    def start_server(self):
        server = ""
        port = 5555
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.byte_length = 2048
        try:
            self.server_socket.bind((server, port))
        except socket.error as e:
            str(e)
        self.server_socket.listen()
        print("Waiting for a connection, Server Started")

    def threaded_engine(self):
        self.game_objects.append(Ball(0)) # load a ball into the game
        while len(self.game_objects) < 3:
            if len(self.game_objects) == 1:
                print('waiting for player 1 to join')
            else:
                print('Waiting for player 2 to join')
            time.sleep(0.5)
        while True:
            self.update()
            time.sleep(0.016) # or 60 fps

    def threaded_player(self, conn, id):
        self.game_objects.append(Player(id))
        msg_index = 0
        first_send = {
            "msg_id" : msg_index,
            "msg" : "setup",
            "player_id" : id
        }
        json_data = json.dumps(first_send)
        conn.send(json_data.encode())
        while True:
            try:
                recv_data = json.loads(conn.recv(self.byte_length))
            except:
                break
            if not recv_data:
                print("Disconnected")
                break
            if recv_data['msg'] == 'playing':
                self.input_buffer[id] = (recv_data)
            json_data = json.dumps(self.output_buffer)
            conn.send(json_data.encode())
        print("Lost connection")
        conn.close()

    def update(self):
        for index, element in enumerate(self.game_objects):
            if index == 0: # first check if the ball, and needs to bounce
                element.check_bounce(self.output_buffer)
            outputdata = element.update(self.input_buffer[index])
            self.output_buffer[outputdata["id"]] = outputdata

    def add_player(self, id):
        self.game_objects[id] = Player(id)

if __name__ == '__main__':
    pong_server = PongServer()
    pong_server.run()