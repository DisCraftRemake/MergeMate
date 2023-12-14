from src.classes.config.configManager import ConfigManager

class Game:
    """
    NO NEED TO INIT

    """
    def __init__(self):
        self.user_config = ConfigManager("user_config.yaml")
        self.game_config = ConfigManager("config.yaml")
        # load entities, load items

    def getDifficulty(self) -> int:
        return self.user_config.getInt("options.difficulty")

    def getDisplaySize(self) -> tuple:
        return (
            self.user_config.getInt("options.width"),
            self.user_config.getInt("options.height")
        )


