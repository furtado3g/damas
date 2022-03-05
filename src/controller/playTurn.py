
class PlayTurn:

    def __init__(self):
        self.__turn = 0

    def getTurn(self):
        return self.__turn

    def incrementTurn(self):
        self.__turn += 1