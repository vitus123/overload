class Building:
    def __init__(self):
        self.numberOfFloors = 2
        self.buildingType = 'дом'

    def setNewNumberOfFloors(self , floors):
        self.numberOfFloors = floors
        print(f'Теперь в доме {self.numberOfFloors} этажей')

    def setNewBuildingType(self , type):
        self.buildingType = type
        print(f'Теперь строение это {self.buildingType}')

    def __eq__(self, other):
        return  (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType)


myHome = Building()
otherHome = Building()

if myHome == otherHome:
    print('Похожие строения')
else:
    print('Это разные строения')

myGarage = Building()
myGarage.setNewNumberOfFloors(1)
myGarage.setNewBuildingType('гараж')

if myHome == myGarage:
    print('Похожие строения')
else:
    print('Это разные строения')


