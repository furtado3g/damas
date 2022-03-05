import imp


from src.controller.board import Board

class Game:
    
    def __init__(self):
        self.__board = Board()
        self.__player1 = None
        self.__player2 = None
        self.__turn = 0
        self.__winner = None
        self.__loser = None
    
    def getBoard(self):
        return self.__board

    def getPlayer1(self):
        return self.__player1

    def getPlayer2(self):
        return self.__player2

    def getTurn(self):
        return self.__turn

    def getWinner(self):
        return self.__winner

    def getLoser(self):
        return self.__loser
         
    def setPlayer1(self,player):
        self.__player = player
                
    def setPlayer2(self,player):
        self.__player = player
    
    def setTurn(self,turn):
        self.__turn = turn

    def setWinner(self,player):
        self.__winner = player

    def setLoser(self,player):
        self.__loser = player

    def playTurn(self,command = None):
        None

