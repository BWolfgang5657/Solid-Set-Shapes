from abc import ABC, abstractmethod

class Solid(ABC):
    __ID = -1
    def __init__(self, kind, color = 'red'):
        self.__kind = kind
        self.__color = color
        Solid.__ID+=1
        self.__ID = Solid.__ID
    def getKind(self):
        return self.__kind
    def getColor(self):
        return self.__color
    def getID(self):
        return self.__ID
    def setColor(self, new):
        self.__color = new
    def __str__(self):
        return f'Solid ID: {self.getID()}\nSolid Kind: {self.getKind()}\nSolid Color: {self.getColor()}'
    @abstractmethod
    def getVolume(self):
        pass