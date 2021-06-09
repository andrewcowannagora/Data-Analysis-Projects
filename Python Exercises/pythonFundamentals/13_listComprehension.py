change = [0.01, 0.1, 0.25, 0.25, 0.1, 0.01, 0.01, 0.25, 0.05]

# Normal loop
dimes = []
for coin in change:
    if coin == 0.1:
        dimes.append(coin)

# List comprehension
dimes = [coin for coin in change if coin == 0.1]

# Conditional part of comprehension is optional
investment = [coin * 1.1 for coin in change]

# List comprehension can be nested (but gets complicated/confusing)
cars = ['camry', 'bronco', 'tesla', 'fusion']
colors = ['red', 'white', 'blue']

colorCars = [f'{color} {car}' for car in cars for color in colors]

colorCars = []
for car in cars:
    for color in colors:
        colorCars.append(f'{color} {car}')
