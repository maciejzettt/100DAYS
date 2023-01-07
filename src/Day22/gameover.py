class GameOver(Exception):
    def __init__(self, message: str):
        super(GameOver, self).__init__(message)
