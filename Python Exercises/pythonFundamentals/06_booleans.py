# Simple booleans
True
False

# Falsey values
bool([])
bool({})
bool('')
bool(0)
bool(None)

# Truthy values
bool(['mirror', 'towel'])
bool({'mirror': 3})
bool('rug')
bool(-23)

# Booleans with conditionals
myList = []
if myList:
    print(myList)

myList = [23, 12, 14]
if myList:
    print(myList)

# Boolean operations
2 == 1
2 == 2
2 != 1
2 != 2
2 > 1
1 > 2
2 >= 1
2 >= 2
2 < 1
1 < 2
2 <= 1
2 <= 2

# Combining booleans
True and False
True or False
[] or True
[] or False
('this' or False) and ([] or 0)

# Lazy evaluation
True or error
error or True
True and error
error and True

# Negating booleans
not True
not False
myList = []
if not myList:
    print('You have no list!')

# Is
myFalseyVal = 0
if myFalseyVal:
    print('I want to print this')

if myFalseyVal is not None:
    print('Now I can print this')

myFirstList = [1, 2, 3]
mySecondList = [1, 2, 3]
myFirstList == mySecondList
myFirstList is mySecondList

# No need to test for boolean equality
if (3 > 2) == True:
    print('Do not repeat yourself')

if 3 > 2:
    print('This works just as well')
