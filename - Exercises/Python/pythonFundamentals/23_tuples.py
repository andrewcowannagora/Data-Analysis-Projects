# Create an empty tuple
myTuple = tuple()

# Create a tuple with values
myTuple = (1, 2, 3)
myTuple = 1, 2, 3  # Parentheses are optional
myTuple = tuple([1, 2, 3])
myTuple = 1  # This is not a tuple!
myTuple = 1,  # This is a tuple

# You can loop through tuples
instruments = ('banjo', 'drums', 'harmonica', 'trumpet', 'saxophone')
for instrument in instruments:
    print(instrument)

# Tuples can be converted to lists
instruments = list(instruments)
instruments.append('flute')

# Access items in a tuple
movies = ('Django Unchained', 'Anaconda', 'Free Willy', 'Matilda', 'Lion King', 'Up')
movies[0]
movies[:3]
