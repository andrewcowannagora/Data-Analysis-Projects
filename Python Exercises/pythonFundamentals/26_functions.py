# Create a function
def getAWord():  # Functions can have 0 or more parameters
    return 'word'  # Functions typically return a value

def getFloor(numerator, denominator):  # This is a somewhat more useful function
    return numerator // denominator

# Call a function
getFloor(10, 3)
getFloor(10, 2)
getFloor(23192, 47)
getFloor(10)  # You must pass in the same number of arguments that are required by the function

# Functions don't need to return a value
myCar = {'milesDriven': 90871, 'gallonsRemaining': 14, 'gasMileage': 22, 'nextOilChangeMileage': 100000}


def driveCar(car, milesToDrive):
    car['milesDriven'] += milesToDrive
    car['gallonsRemaining'] -= milesToDrive / car['gasMileage']

def isOilChangeRequired(car):
    return car['milesDriven'] > car['nextOilChangeMileage']

driver1 = {'name': 'Todd', 'drivingMinutes': 123}
driver2 = {'name': 'Maddie', 'drivingMinutes': 0}
def switchDriver(currentDriver, passenger, switchMinutes):
    if currentDriver['drivingMinutes'] > switchMinutes:
        print('Switching drivers')
        currentDriver['drivingMinutes'] = 0
        return passenger  # Return statements will exit the function
    print('Keeping the same driver')
    return currentDriver

# Functions can call other functions
def driveCar(car, milesToDrive):
    car['milesDriven'] += milesToDrive
    car['gallonsRemaining'] -= milesToDrive / car['gasMileage']
    if isOilChangeRequired(car):
        print('Time to get an oil change!')


# Functions can be defined within other functions
def driveCar(car, milesToDrive):
    def getMilesToNextFill(gallonsBeforeFill):
        return (car['gallonsRemaining'] - gallonsBeforeFill) * car['gasMileage']

    while milesToDrive:
        milesToNextFill = getMilesToNextFill(5)
        print(f'You have {milesToNextFill} before needing a refill')
        if milesToDrive > milesToNextFill:
            print('Filling up on gas')
            milesToDrive -= milesToNextFill
            car['gallonsRemaining'] = 14
            car['milesDriven'] += milesToNextFill
        else:
            car['gallonsRemaining'] -= milesToDrive / car['gasMileage']
            car['milesDriven'] += milesToDrive
            milesToDrive = 0

    if isOilChangeRequired(car):
        print('Time to get an oil change!')


# Parameters and arguments
# A prime number is a number that is only divisible by itself an 1
def isPrimeNumber(num):  # num is a parameter
    for divisor in range(num):
        if divisor in (0, 1):
            continue
        if num % divisor == 0:
            return False
    return True

isPrimeNumber(7)  # 7 is an argument
isPrimeNumber(8)  # 8 is an argument
isPrimeNumber(127)  # 127 is an argument

# Parameters can have a default
def getExponent(num, exponent=2):  # Parameters with defaults must come after those that don't
    return num ** exponent

getExponent(3)
getExponent(3, 4)


def getTempConversion(tempInFarenheit, tempChange, isConvertToCelsius=False, isConvertToKelvin=False):
    newTemp = tempInFarenheit + tempChange
    tempInCelsius = newTemp - 32 * (5 / 9)
    if isConvertToCelsius:
        return tempInCelsius
    if isConvertToKelvin:
        return tempInCelsius + 273.15
    return newTemp

tempInFarenheit, tempChange = (45, 23.1)
argumentDefaults = {'isConvertToCelsius': False, 'isConvertToKelvin': False}
keyWordArguments = {'isConvertToKelvin': True}
for key, val in argumentDefaults.items():
    if key in keyWordArguments:
        print(keyWordArguments[key])
    else:
        print(val)


# Scope - LEGB = Local, Enclosing, Global, Built-in
localRoom = {'keys': 'car', 'wallet': 'money'}
enclosingHouse = {'keys': 'house', 'chairs': 4}
globalCountry = {'house': 26135, 'people': 981234, 'chairs': 38238, 'tempConversion': getTempConversion}
builtInWorld = {'keys': 'space ship', 'people': 71000000000, 'carbon': 238473.2, 'len': len}

def scopeSearch(objectName):
    if objectName in localRoom:
        return localRoom[objectName]
    if objectName in enclosingHouse:
        return enclosingHouse[objectName]
    if objectName in globalCountry:
        return globalCountry[objectName]
    if objectName in builtInWorld:
        return builtInWorld[objectName]
    return f'Error: No object named {objectName} found'

# Global variables
x = 3
y = 4

def getLengthOfList(x):
    print(f'The value of x is {x}')  # Print is a built-in function

    def createList():
        # Enclosing variables
        lengthOfList = x * y  # y is from the global variables
        newList = []
        for num in range(lengthOfList):  # Range is a built-in function
            newList.append(num)
        return newList

    return len(createList())

# Functions vs methods
myHobbies = ['hiking', 'boxing', 'reading']
myOtherList = [1, 2, 3]
myDict = {'this': 2}
myOtherList.append(4)
myHobbies.append('coding')  # method
myDict.append(2)  # Doesn't work
len(myHobbies)  # function
len('this is a string')

# Functions are objects
def pluralize(string, num):
    if num == 1:
        return f'{num} {string}'
    return f'{num} {string}s'

myHouse = {'chair': 4, 'table': 1, 'fork': 8}

def printHouseInventory(house, pluralFn):
    for item, count in house.items():
        print(pluralFn(item, count))

printHouseInventory(myHouse, pluralize)
