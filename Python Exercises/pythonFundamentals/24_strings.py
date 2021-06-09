# Create strings
myDog = 'Shelby'
myLicense = "xyzs-9083"
# thisIsBad = "trs45'

# String characters can be accessed similar to lists
myWords = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
myString = 'Hello world'

myWords[1:3]
myString[1:3]

for char in myWords:
    print(char)

for char in myString:
    print(char)

# You can search for substrings like you would search for a value in a list
'world' in myString

# Strings are immutable
del myString[1]  # Won't work

# String concatenation
combined = 'This' + ' ' + 'is' + 'concatenation'
myWords = ['This', 'is', 'concatenation', 'too']
newCombo = ' '.join(myWords)
newCombo = 'random'.join(myWords)
'My car is a %s and was built in %s' % ('ford', '2013')  # Old way

number = 23
f'Your number is {number}. Multiplied by two, it is {number * 2}'  # New way

# Escaping characters
# thisIsBad = 'This won't work'
thisWillWork = "This won't work"
thisWillWorkToo = 'This won\'t work'

thisIsASpecialCharacter = '\b'
filePath = '\Users\pfb\PycharmProjects\bythonForBusiness\rythonFundamentals'
filePath = r'\Users\pfb\PycharmProjects\bythonForBusiness\rythonFundamentals'