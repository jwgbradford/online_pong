import socket, pickle, time
from game_engine import MyGame
from threading import Thread

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

my_game = MyGame()

def threaded_client(conn, id):
    my_game.add_player(id)
    while len(my_game.game_objects) < 3:
        print('waiting for other client to join')
        time.sleep(1)
    while True:
        try:
            keys = pickle.loads(conn.recv(2048))
            my_game.game_objects[id].move(keys)
            if not data:
                print("Disconnected")
                break
            conn.send(pickle.dumps(my_game.game_data))
        except:
            break

    print("Lost connection")
    conn.close()

def threaded_engine():
    while len(my_game.game_objects) < 3:
        print('waiting for clients to join')
        time.sleep(1)
    while True:
        my_game.update()
        print('running')
        time.sleep(1)

ge = Thread(target=threaded_engine, args=())
ge.start()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr[1])
    x = Thread(target=threaded_client, args=(conn, addr[1]))
    x.start()