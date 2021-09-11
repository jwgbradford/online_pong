import socket
from threading import Thread
from game_objects import Engine

class PongServer():
    def __init__(self) -> None:
        pass

    def run(self):
        self.start_server()
        pong_engine = Engine()
        Thread(target=pong_engine.run, args=()).start()
        player_number = 1
        while True:
            print("Waiting for client, Pong Engine Started")
            conn, addr = self.server_socket.accept()
            print("Connected to:", addr[1])
            pong_engine.new_player(conn, player_number)
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

if __name__ == '__main__':
    pong_server = PongServer()
    pong_server.run()