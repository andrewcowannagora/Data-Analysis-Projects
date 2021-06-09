# Create an empty set
mySet = set()

# Create a set with values
mySet = {1, 2, 4, 'this'}
myOtherSet = set([1, 2, 4, 'this'])

# Items in a set are unique
myUniqueSet = {1, 1, 1, 2, 2, 2, 3, 3, 3}

# Use a set to get rid of duplicate values
notUniqueValues = ['blue', 'red', 'yellow', 'blue', 'blue', 'red', 'orange', 'yellow']
uniqueValues = list(set(notUniqueValues))

uniqueValues = []
for val in notUniqueValues:
    if val not in uniqueValues:
        uniqueValues.append(val)

# Items in a set cannot be mutable
badSet = {'this', ['will', 'not', 'work']}

# Common set methods
mySet = {'volvo', 'tesla', 'ford'}
mySet.add('hyundai')
mySet.update({'chrysler', 'fiat', 'chevrolet'})
mySet.discard('volvo')
mySet.discard('jaguar')  # Won't raise an error even though value is not in set
mySet.remove('ford')
mySet.remove('jaguar')  # Will raise an error
myCar = mySet.pop()

# Check if a value is in a set
if 'fiat' in mySet:
    print('Found the fiat')

# Loop through a set
for carMake in mySet:
    print(carMake)
