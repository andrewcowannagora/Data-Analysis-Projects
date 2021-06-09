# Create a dictionary
myDictionary = {}
alsoMyDictionary = dict()

# You can add values during creation
myDictionary = {
    'uno': 1,
    'dos': 2,
    'tres': 3
}

myDictionary = dict(
    uno=1,
    dos=2,
    tres=3
)

# Dictionaries don't need homogeneous values
aVariable = 'something'
myDictionary = {
    'a': 47,
    'b': None,
    27: 38,
    aVariable: 'else'
}

# Keys can't be mutable
myDictionary = {
    [1, 2]: 47  # This won't work because lists are mutable
}

myDictionary = {
    (1, 2): 47  # This will work because tuples are not mutable
}

# Keys must be unique
myDictionary = {
    'copyKey': 1,
    'copyKey': 2
}

# Dictionaries can be nested
carsInLot = {
    'xyz-1234': {'make': 'volvo', 'model': 'C70', 'year': 2016},
    'vanity1': {'make': 'tesla', 'model': 'X', 'year': 2018},
    'ytpo-345': {'make': 'ford', 'model': 'Fusion', 'year': 2010}
}

# Access dictionary values using keys
carsInLot['xyz-1234']
myKey = 'ytpo-345'
carsInLot[myKey]

carsInLot['123-ytrz']  # This will cause an error because the key doesn't exist

# Update items in a dictionary
carsInLot[myKey]['year'] = 2020

# Add items to a dictionary
carsInLot['123-ytrz'] = {'make': 'kia', 'model': 'Sorento', 'year': 2021, 'state': 'MO'}
carsInLot[myKey]['state'] = 'CO'

# Check if a key is in a dictionary
if 'vanity1' in carsInLot:
    print('Tesla in lot')

# Common dictionary methods and functions
carsInLot['1454-sps']  # This will cause an error
carsInLot.get('1454-sps')
carsInLot.get('1454-sps', 'No car found')

carsInLot.items()
for key, car in carsInLot.items():
    print(f'Car with license {key} is from {car.get("state", "Unknown")}')

carsInLot.values()
carsInLot.keys()

towedCar = carsInLot.pop('vanity1')

del carsInLot['xyz-1234']
