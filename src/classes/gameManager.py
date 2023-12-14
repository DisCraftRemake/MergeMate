from main import Game

class GameManager:
    _game_instance = None

    @classmethod
    def get_game_instance(cls):
        if cls._game_instance is None:
            cls._game_instance = Game()
        return cls._game_instance
