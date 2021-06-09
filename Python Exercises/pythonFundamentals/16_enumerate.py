headers = ['name', 'age', 'gender', 'isTeacher']
rows = [
    ['Jerry', 34, 'M', False],
    ['Jane', 53, 'F', False],
    ['Matt', 41, 'M', True]
]

for idx, header in enumerate(headers):
    for row in rows:
        print(f'{header}: {row[idx]}')
