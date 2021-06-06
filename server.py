import socket, pickle, time
from game_engine import MyGame
from threading import Thread

def threaded_client(conn, id):
    my_game.add_player(id)
    conn.send(pickle.dumps(id))
    while True:
        try:
            keys = pickle.loads(conn.recv(4096))
            if not keys:
                print("Disconnected")
                break
            if my_game.game_objects['msg body'] == 'Running':
                my_game.game_objects[id].move(keys)
            conn.send(pickle.dumps(my_game.game_data))
        except:
            break
    print("Lost connection")
    conn.close()

def threaded_engine():
    while len(my_game.game_objects) < 4:
        if len(my_game.game_objects) < 3:
            print('waiting for clients to join')
        else:
            print('Waiting for other client to join')
        time.sleep(0.5)
    my_game.game_objects['msg body'] = 'Running'
    while True:
        my_game.update()
        time.sleep(0.01)

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

my_game = MyGame()

ge = Thread(target=threaded_engine, args=())
ge.start()

while True:
    print("Waiting for client, Engine Started")
    conn, addr = s.accept()
    print("Connected to:", addr[1])
    x = Thread(target=threaded_client, args=(conn, addr[1]))
    x.start()