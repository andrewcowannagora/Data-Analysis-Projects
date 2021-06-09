# Create a list
myList = []
myOtherList = list()

# Create a list with values
myList = [1, 2, 3]
myOtherList = list([1, 2, 3])

# Values don't have to be homogeneous
myNumber = 2.89
myList = [1, None, {'this': 'dict'}, myNumber]

# Lists can be nested
myNestedList = [1, 2, 3, [4, 5, ['this', 'that'], 6], 9]

# Accessing items in a list
myList = ['first item', 'second item', 'third item', 'fourth item']
myList[0]  # List index starts at 0
myList[2]
myList[-1]  # Negative indexes can be used to start at the end of the list
myList[-2]
myList[5]  # Error when index is greater than or equal to list length
myList[0:2]  # Start position (inclusive), end position (exclusive)
myList[:3]  # When either number is left blank, defaults are start and end of list
myList[1:]
myList[:]
myList[0:-2]  # Negative numbers can be used

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList[1:9:2]  # A third value can be added to indicate step size

# Items can be updated using the list index
myList[2] = 100012

# Common list methods and functions
myList = ['first item', 'second item', 'third item', 'fourth item']

myList.append('fifth item')
myList.insert(2, 'apples')
myList.extend(['some', 'other', 'list'])
[1, 2] + [3, 4, 5]

myVal = myList.pop(4)
myList.remove('second item')
del myList[0]

myNumericList = [2, 34, 1, 10, 5, 5, 6, 999]
myNumericList.sort()
myAlphabeticList = ['zebra', 'possum', 'wombat', 'cat', 'whale']
myNewList = sorted(myAlphabeticList)

len(myNewList)

# Check if an item is in a list
'zebra' in myNewList
if 'dog' in myNewList:
    print('Woof')