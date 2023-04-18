import math
from abc import ABC, abstractmethod
from solid import Solid

class Sphere(Solid):
    def __init__(self, radius, color='red'):
        __kind = 'Sphere'
        super().__init__(__kind, color)
        self.__radius = float(radius)
        self.__ID = super().getID()
    def getRadius(self):
        return self.__radius
    def setRadius(self, new):
        self.__radius = new
    def getVolume(self):
        return (4/3 * math.pi *  (self.__radius**3))
    def __str__(self):
        return f'Solid ID: {super().getID()}\nSolid Kind: {super().getKind()}\nSolid Color: {super().getColor()}\nVolume: {self.getVolume()}\nRadius: {self.getRadius()}'
    
class Cone(Solid):
    def __init__(self, radius, height, color='red'):
        __kind = 'Cone'
        super().__init__(__kind, color)
        self.__radius = float(radius)
        self.__height = float(height)
    def getRadius(self):
        return self.__radius
    def getHeight(self):
        return self.__height
    def setRadius(self, new):
        self.__radius = new
    def setHeight(self, new):
        self.__height = new
    def getVolume(self):
        return (1/3 * math.pi * (self.__radius**2) * self.__height)
    def __str__(self):
        return f'Solid ID: {super().getID()}\nSolid Kind: {super().getKind()}\nSolid Color: {super().getColor()}\nVolume: {self.getVolume()}\nRadius: {self.getRadius()}\nHeight: {self.getHeight()}'
