def multiplyByTwo(val):
    return val * 2

def isGreaterThanTwo(val):
    return val > 2

myNums = [1, 2, 3, 4]

map(multiplyByTwo, myNums)
map(isGreaterThanTwo, myNums)

newList = []
for num in myNums:
    newList.append(multiplyByTwo(num))
