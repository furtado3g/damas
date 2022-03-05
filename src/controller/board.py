class Board:

    def __init__(self, size):
        self.__size = size
        #self.__board = [[None for x in range(size)] for y in range(size)]
        self.__board = []
        for x in range(size):
            horizontal = []
            for y in range(size):
                horizontal.append(None)
            self.__board.append(horizontal)
    
    def getSize(self):
        return self.__size

    def getBoard(self):
        return self.__board
        
    def setPiecePosition(self, piece, x, y):
        self.__board[x][y] = piece

    def itHaveAPiece(self, x, y):
        if self.__board[x][y] is None:
            return False
        else:
            return True
        #return self.__board[x][y] is not None

    def getPiece(self, x, y):
        return self.__board[x][y]

    