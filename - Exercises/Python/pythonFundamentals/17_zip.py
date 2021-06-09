zip([1, 2], ['one', 'two'])
zip([1, 2], ['one', 'two'], ['uno', 'dos'])

headers = ['name', 'age', 'gender', 'isTeacher']
rows = [
    ['Jerry', 34, 'M', False],
    ['Jane', 53, 'F', False],
    ['Matt', 41, 'M', True]
]

enumerate(headers)
zip(range(len(headers)), headers)

for row in rows:
    for header, val in zip(headers, row):
        print(f'{header}: {val}')