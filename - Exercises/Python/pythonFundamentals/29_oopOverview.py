import inspect

def getClassStructure(item):
    return inspect.getmro(type(item))

getClassStructure(1.1)
getClassStructure(True)
getClassStructure({'this', 'that'})
getClassStructure({'apples': 2, 'oranges': 3})
getClassStructure(['ford', 'mazda'])
getClassStructure(None)
getClassStructure((1, 2, 3))
getClassStructure(1)

def myFunc(x):
    return x + 1

getClassStructure(myFunc)

myLambda = lambda x: x + 1
getClassStructure(myLambda)

def myGenerator(x):
    yield x + 1

myGen = myGenerator(1)
getClassStructure(myGen)
