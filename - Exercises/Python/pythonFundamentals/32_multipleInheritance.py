class Human:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def move(self):
        print('Walking')

    def eat(self):
        print('Eating')


class Eat:
    def eat(self):
        print('Chewing')

    def getFood(self):
        print('Found something in the fridge')


class Baby(Human, Eat):

    def move(self):
        print('Crawling')

# Search
# 1) Baby
# 2) Human or Eat
# 3) object
# 4) not found - error

myBaby = Baby(1, 'Bill')
myBaby.move()
myBaby.getFood()
myBaby.eat()
