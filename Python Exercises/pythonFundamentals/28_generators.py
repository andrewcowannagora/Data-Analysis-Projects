# Generators save memory
def addOne(val):
    return val + 1

generator = {
    'currentVal': 0,
    'transformFn': addOne
}

def getNextVal(generator):
    nextVal = generator['transformFn'](generator['currentVal'])
    generator['currentVal'] = nextVal
    return nextVal

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a generator
def myGenerator(startingNumber):
    newNumber = startingNumber
    print(f'Starting number is {newNumber}')
    while True:
        newNumber += 1
        yield newNumber  # This is where the generator stops until "next" is called again
        print('I execute after next call')

# Get a value from a generator
generator = myGenerator(3)
next(generator)

# Generators only get the next value (they can't go backwords) and they can only loop through once
def myDailyRoutine(routine):
    for activity in routine:
        yield activity

myRoutine = ['eat', 'work', 'read', 'sleep']
getRoutine = myDailyRoutine(myRoutine)
next(getRoutine)
next(getRoutine)
next(getRoutine)
next(getRoutine)
next(getRoutine)

for activity in myRoutine:
    print(activity)
print('Exit loop')

try:
    iterator = myRoutine.__iter__()
    while True:
        print(next(iterator))
except StopIteration:
    print('Exit loop')