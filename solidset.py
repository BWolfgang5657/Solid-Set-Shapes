class SolidSet():
    def __init__(self):
        self.__solids = []
    def getSolids(self):
        return self.__solids
    def getSolid(self, ID):
        for index in self.__solids:
            if ID == index.getID():
                return index
        else:
            return None
    def getSpheres(self):
        sphereList = []
        for index in self.__solids:
            if index.getKind() == 'Sphere':
                sphereList.append(index)
        return sphereList
    def getCones(self):
        coneList = []
        for index in self.__solids:
            if index.getKind() == 'Cone':
                coneList.append(index)
        return coneList
    def addSolid(self, solid):
        self.__solids.append(solid)
    def getTotalVolume(self):
        total = 0
        for index in self.__solids:
            total+=index.getVolume()
        return total