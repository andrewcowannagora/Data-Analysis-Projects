x = 2
y = 3
z = []

# if statement
if x and y and z:
    print('This')

if x or y or z:
    print('That')

# nested if statements
if x:
    print('I have x')
    if z:
        print('I have z')
        if y:
            print('I have y')

if x:
    print('I have x')
    if z:
        print('I have z')
    if y:
        print('I have y')

# if / elif / else
if x:
    print('I have x')
elif z:
    print('I have z')

if z:
    print('I have z')
elif y:
    print('I have y')

if z:
    print('z')
elif 3 > 4:
    print('This is not true')
elif {}:
    print('This is falsey')
else:
    if 3 < 4:
        print('I know math')
    print('I finally printed something')