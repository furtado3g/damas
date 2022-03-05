class Piece:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__isAlive = True
        self.__isQueen = False
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def getIsAlive(self):
        return self.__isAlive

    def getIsQueen(self):
        return self.__isQueen

    def setIsAlive(self,isAlive=False):
        self.__isAlive = isAlive

    def setIsQueen(self,isQueen=True):
        self.__isQueen = isQueen

    def move(self,x,y):
        self.__x = x
        self.__y = y
        

