import random

myRandomObjects = ['towel', 'computer', 'dog', 'guitar']

def pickRandomObject(objects):
    return random.choice(objects)

def printFoundObject(obj):
    print(f'I found a {obj}')

for _ in range(5):
    printFoundObject(pickRandomObject(myRandomObjects))

randomOccurrences = {}
for _ in range(1000):
    obj = pickRandomObject(myRandomObjects)
    if obj not in randomOccurrences:
        randomOccurrences[obj] = 1
    else:
        randomOccurrences[obj] += 1

for obj, count in randomOccurrences.items():
    print(f'{obj} was found {count} times')

list