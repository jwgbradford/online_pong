import math, pygame, json
from threading import Thread
from random import randint
from pong_constants import WIDTH, HEIGHT

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

class Engine():
    def __init__(self) -> None:
        self.game_objects = []
        self.output_buffer = {}
        self.input_buffer = {}

    def run(self):
        pygame.init()
        self.game_objects.append(Ball(0)) # load a ball into the game
        clock = pygame.time.Clock()
        while len(self.game_objects) < 3:
            if len(self.game_objects) == 1:
                print('waiting for player 1 to join')
            else:
                print('Waiting for player 2 to join')
            clock.tick(1)
        while True:
            self.update()
            clock.tick(60)

    def new_player(self, conn, player_number):
        self.game_objects.append(Player(player_number))
        connected_player = Thread(target=self.threaded_player, args=(conn, player_number))
        connected_player.start()

    def update(self):
        for index, element in enumerate(self.game_objects):
            if index == 0: # first check if the ball, and needs to bounce
                element.check_bounce(self.output_buffer)
            outputdata = element.update(self.input_buffer[index])
            self.output_buffer[outputdata["id"]] = outputdata

    def threaded_player(self, conn, id):
        msg_index = 0
        first_send = {
            "msg_id" : msg_index,
            "msg" : "setup",
            "player_id" : id,
            "data" : {
                "height" : HEIGHT,
                "width" : WIDTH}
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
