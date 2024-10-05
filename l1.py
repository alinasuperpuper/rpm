class GameState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameState, cls).__new__(cls)

            cls._instance.level = 1
            cls._instance.score = 0
            cls._instance.time = 0

        return cls._instance

    def update_state(self, level=None, score=None, time=None):
        if level is not None:
            self.level = level

        if score is not None:
            self.score = score

        if time is not None:
            self.time = time

    def __str__(self):
        return f'level: {self.level}, score: {self.score}, time: {self.time}'


game_state1 = GameState()
print(game_state1)

game_state1.update_state(level=2, score=100, time=30)

game_state2 = GameState()
print(game_state2)
print(id(game_state1), id(game_state2))
