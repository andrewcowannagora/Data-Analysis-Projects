change = [0.01, 0.1, 0.25, 0.25, 0.1, 0.01, 0.01, 0.25, 0.05]

quarters = []
for coin in change:
    if coin != 0.25:
        print('This is not a quarter')
        continue
    quarters.append(coin)

for coin in change:
    if coin == 0.01:
        change.remove(0.01)
        print('Gave away a penny')
        break
