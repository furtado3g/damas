from src.controller.playTurn import playTurn

class Player:
    def __init__(self,name):
        self.__name = name
        self.__turn = playTurn()
    
    def getName(self):
        return self.__name

    def getTurn(self):
        return self.__turn.getTurn()

    def incrementTurn(self):
        self.__turn.incrementTurn()
    
    def playTurn(self,command = None):
        None