x = 3

if x > 2:
    print('This is true')
else:
    print('This will not print')

print('This is true') if x > 2 else print('This will not print')

y = 4 if x < 2 else 10

myOtherList = None
myList = myOtherList if myOtherList is not None else [1, 2]
