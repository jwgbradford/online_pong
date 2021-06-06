from game_objects import Player, Ball # need to add players and balls to the game engine

class MyGame:
    def __init__(self):
        width = 500
        height = 500
        self.game_objects = self.add_game_objects()
        self.game_data = {}
    
    def update(self):
        self.game_objects['ball'].move()
        for id in self.game_objects:
            self.game_data[id] = self.game_objects[id].pos

    def add_game_objects(self):
        game_obj = {}
        game_obj['ball'] = Ball()
        return game_obj

    def add_player(self, id):
        self.game_objects[id] = Player()