from src.classes.gameManager import GameManager

class Entity:
    def __init__(self, strength: int, health: int):
        self.strength = strength
        self.health = health
        self.game = GameManager.get_game_instance()

    @property
    def game(self):
        return self.game

    @game.setter
    def game(self, value):
        self.game = value

    @property
    def strength(self):
        return self.strength

    @strength.setter
    def strength(self, value):
        self.strength = value

    @property
    def health(self):
        return self.health

    @health.setter
    def health(self, value):
        self.health = value

    def attack(self) -> int:
        return self.game.getDifficulty() * self.strength
