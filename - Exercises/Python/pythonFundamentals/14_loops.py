# For loop
backpackItems = ['sleeping bag', 'pillow', 'shoes', 'jacket', 'peanut butter', 'tent']

for item in backpackItems:
    print(f'Do you have {item}?')

# While loop
itemsCount = 0
while itemsCount < len(backpackItems):
    print(f'Yes, I have {backpackItems[itemsCount]}')
    itemsCount += 1
    print(itemsCount)

swimmingDistance = 0
distancePerMinute = 100
swimmingMinutes = 60

while swimmingMinutes:
    swimmingDistance += distancePerMinute
    swimmingMinutes -= 1

# Nesting
daysInMonth = 30
activities = ['eat', 'sleep', 'work']

for day in range(daysInMonth):
    for activity in activities:
        print(f'Day {day}: I {activity}')
