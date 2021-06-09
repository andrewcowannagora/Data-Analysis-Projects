# Everything is an object and an object is a class
myList = list([1, 2, 3])  # list is a class, myList is an instance of a class
myInt = 1  # 1 is an instance of an integer
myOtherInt = 2  # 2 is an instance of an integer

# Create a class
class Car:  # Classes start with a capital letter (Pascal case)
    def drive(self):
        print('Driving')

class Car(object):
    speedLimit = 120
    def drive(self):
        print('Driving')

myCar = Car()
myCar.drive()

yourCar = Car()
yourCar.drive()

myCar.drive()  # Method (class function)
myCar.speedLimit  # Attribute (class variable)

# Initialization
class Car(object):

    def __init__(self, maxSpeed, make, model):
        self.maxSpeed = maxSpeed
        self.make = make
        self.model = model

    def drive(self):
        print(f'Driving my {self.make}, {self.model}')

myCar = Car(150, 'Ford', 'Fusion')
yourCar = Car(100, 'Volvo', 'C70')
myCar.__dict__
yourCar.__dict__
myCar.drive()
yourCar.drive()

# "self" stores the "state" of an object
# basically a dictionary of all methods and attributes
class Car(object):

    def __init__(self, maxSpeed, make, model, color):
        self.maxSpeed = maxSpeed
        self.make = make
        self.model = model
        self.color = color

    def drive(self):
        print('Driving')

    def paintJob(self, newColor):
        self.color = newColor

    def isCarColor(self, colorToCheck):
        return self.color == colorToCheck

notAClassCar = {'maxSpeed': 150, 'make': 'Ford', 'model': 'Fusion', 'color': 'red'}

def paintJob(car, newColor):
    car['color'] = newColor

# Class instances are stateful
myCar = Car(150, 'Ford', 'Fusion', 'red')
myCar.isCarColor('red')
myCar.paintJob('blue')
myCar.isCarColor('red')

# Not all initialization arguments need to be assigned to self
class Car(object):

    def __init__(self, maxSpeed, make, model, color, year):
        self.maxSpeed = maxSpeed
        self.make = make
        self.model = model
        self.color = color
        self.isUnderWarranty = year > 2016
        self.age = 2021 - year

    def drive(self):
        print('Driving')

    def paintJob(self, newColor):
        self.color = newColor

    def isCarColor(self, colorToCheck):
        return self.color == colorToCheck


# Inheritance and dot notation
bool  # Mac: Cmd + B  PC: Ctrl + B to get to the bool class

# Search
# 1) ElectricCar
# 2) Car
# 3) object
# 4) not found - error

class ElectricCar(Car):

    def chargeBattery(self):
        print('Charging')

    def drive(self):  # Methods and attributes can be overriden
        print('Driving electric')

myElectricCar = ElectricCar(100, 'Tesla', 'S', 'Gray', 2018)
myNormalCar = Car(120, 'Ford', 'Fusion', 'Red', 2016)

myElectricCar.drive()
myNormalCar.drive()
myElectricCar.chargeBattery()
myNormalCar.chargeBattery()
myElectricCar.isUnderWarranty
myNormalCar.isUnderWarranty


# Super method
class ElectricCar(Car):

    def __init__(self, maxSpeed, make, model, color, year, chargeLevel):
        self.chargeLevel = chargeLevel
        super().__init__(maxSpeed, make, model, color, year)

    def chargeBattery(self):
        print('Charging')

    def drive(self):  # Methods and attributes can be overriden
        print('Driving electric')
        super().drive()
