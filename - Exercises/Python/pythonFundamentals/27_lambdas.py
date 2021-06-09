# Create a lambda
myDictionary = {'apple': 4, 'orange': 3, 'lemon': 10}
myNewDictionary = {}

getVal = lambda key: myDictionary[key]

def getVal(key):
    return myDictionary[key]

for key in myDictionary:
    myNewDictionary[key] = getVal(key)

# Lambdas do not need to be assigned to a variable
plurals = list(map(lambda item: f'{item}s', myDictionary.keys()))

# Lambdas can have any number of parameters
repeater = lambda phrase, repeat, name: f'{" ".join([phrase] * repeat)} {name}'
repeater('wake up', 10, 'Todd')
