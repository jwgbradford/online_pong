from game_objects import Player, Ball

class MyGame:
    def __init__(self):
        width = 500
        height = 500
        self.game_objects = self.add_game_objects()
        self.game_data = {}
    
    def update(self):
        self.game_objects['ball'].move()
        for id in self.game_objects:
            if id == 'msg body':
                self.game_data[id] = self.game_objects[id]
            elif id == 'ball':
                self.game_data[id] = self.game_objects[id].pos
            else:
                self.game_data[id] = self.game_objects[id].y

    def add_game_objects(self):
        game_obj = {}
        game_obj['msg body'] = 'Waiting for other client'
        game_obj['ball'] = Ball()
        return game_obj

    def add_player(self, id):
        self.game_objects[id] = Player(id)