from collections import defaultdict

carsInLot = {
    'xyz-1234': {'make': 'volvo', 'model': 'C70', 'year': 2016},
    'vanity1': {'make': 'tesla', 'model': 'X', 'year': 2018},
    'ytpo-345': {'make': 'ford', 'model': 'Fusion', 'year': 2010},
    'mxrd-304': {'make': 'mazda', 'model': 'RX6', 'year': 2013},
    'mzsdtr-05': {'make': 'ford', 'model': 'F150', 'year': 2016}
}

carsByMake = defaultdict(list)
for licensePlate, car in carsInLot.items():
    car['license'] = licensePlate
    carsByMake[car['make']].append(car)

carsByMake = {}
for licensePlate, car in carsInLot.items():
    car['license'] = licensePlate
    carMake = car['make']
    if carMake not in carsByMake:
        carsByMake[carMake] = list()
    carsByMake[carMake].append(car)

peopleWaitingInLine = defaultdict(int)

for newPerson in range(10):
    for person in peopleWaitingInLine.keys():
        peopleWaitingInLine[person] += 1
    peopleWaitingInLine[f'Person {newPerson}'] += 1