class Car(object):

    def __init__(self, maxSpeed, make, model, color, year):
        self.maxSpeed = maxSpeed
        self.make = make
        self.model = model
        self.color = color
        self.isUnderWarranty = year > 2016
        self.year = year
        self.age = 2021 - year

    def drive(self):
        print('Driving')

    def paintJob(self, newColor):
        self.color = newColor

    def isCarColor(self, colorToCheck):
        return self.color == colorToCheck

def printSpecialMethods(obj):
    for method in obj.__dir__():
        if '__' in method:
            print(method)

myCar = Car(150, 'Mazda', 'Miata', 'gold', 2010)
myOtherCar = Car(120, 'Toyota', 'Prius', 'silver', 2012)

class Car(object):

    def __init__(self, maxSpeed, make, model, color, year):
        self.maxSpeed = maxSpeed
        self.make = make
        self.model = model
        self.color = color
        self.isUnderWarranty = year > 2016
        self.year = year
        self.age = 2021 - year

    def drive(self):
        print('Driving')

    def paintJob(self, newColor):
        self.color = newColor

    def isCarColor(self, colorToCheck):
        return self.color == colorToCheck

    def __gt__(self, other):
        return self.maxSpeed > other.maxSpeed

    def __lt__(self, other):
        return self.make < other.make