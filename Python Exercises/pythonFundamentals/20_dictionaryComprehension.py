carsInLot = {
    'xyz-1234': {'make': 'volvo', 'model': 'C70', 'year': 2016},
    'vanity1': {'make': 'tesla', 'model': 'X', 'year': 2018},
    'ytpo-345': {'make': 'ford', 'model': 'Fusion', 'year': 2010},
    'mxrd-304': {'make': 'mazda', 'model': 'RX6', 'year': 2013},
    'mzsdtr-05': {'make': 'ford', 'model': 'F150', 'year': 2016}
}

fordCars = {licensePlate: car for licensePlate, car in carsInLot.items() if car['make'] == 'ford'}

fordCars = {}
for licensePlate, car in carsInLot.items():
    if car['make'] == 'ford':
        fordCars[licensePlate] = car

models = {licensePlate: car['model'] for licensePlate, car in carsInLot.items()}

models = {}
for licensePlate, car in carsInLot.items():
    models[licensePlate] = car['model']
