
COOK_TARGETS = {
   'rare': 120,
   'medium': 130,
   'well done': 140
}


def grillSteak(steakOrders, temperature):
   """Get a list of Steaks, each heated to the ordered cook target.

   :param list steakOrders: A list of steak orders. Each item must be a key in COOK_TARGETS.
   :param int temperature: An integer indicating the tem
   :return list: A list of Steak objects heated to the temperature based on the order.
   """
   steaks = []
   for steakOrder in steakOrders:
       steaks.append(Steak(steakOrder))  # Create a Steak object based on each order

   grill = Grill(temperature)
   grill.startGrill()
   meatTempIncrease = grill.getTempIncrease()

   """Increase the temperature of each steak.
   Once all steaks are done, exit the loop.
   I really like steaks. And I could go on for many
   lines about the right way to cook steaks.
   """
   steaksNotDone = True
   while steaksNotDone:
       for steak in steaks:
           if not steak.isDone():
               print(f'Increasing the steak temperature by {meatTempIncrease}')
               steak.increaseTemperature(meatTempIncrease)
       steaksNotDone = any([not steak.isDone() for steak in steaks])

   print('Steaks are ready to serve')
   return steaks


class Grill:
   def __init__(self, temperatureTarget):
       self.temperature = 0
       self.temperatureTarget = temperatureTarget

   def startGrill(self):  # Increases the temperature of the grill until the temperatureTarget is achieved
       print('Starting the grill')
       while not self.isReady():
           self.increaseTemperature()
           print(f'New temperature is {self.temperature}')

       print('Grill is ready')


   def increaseTemperature(self):
       self.temperature += 50

   def isReady(self):
       return self.temperature >= self.temperatureTarget

   def getTempIncrease(self):
       return self.temperature / 20


class Steak:
   def __init__(self, cookTarget):
       self.temperature = 0
       self.internalTempTarget = COOK_TARGETS[cookTarget]

   def increaseTemperature(self, tempIncrease):
       self.temperature += tempIncrease

   def isDone(self):
       return self.temperature >= self.internalTempTarget


grillSteak(['rare', 'rare', 'well done', 'medium', 'rare', 'medium'], 400)
