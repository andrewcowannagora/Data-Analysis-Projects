# import collections  # import an entire package
# import math  # import an entire module
#
# myDefaultDict = collections.defaultdict(int)
# myExponent = math.pow(2, 4)
# print(myDefaultDict)
# print(myExponent)
#
# Specific objects can be imported from a package or module
# from collections import defaultdict, namedtuple
# from math import pow
#
# myDefaultDict = defaultdict(int)
# myNamedTuple = namedtuple('Car', 'engine, color, maxSpeed')
# myExponent = pow(2, 4)
#
# All objects can be "unpacked"
# import collections
#
# myDefaultDict = collections.defaultdict(int)
#
# def defaultdict(val):
#     print('This is confusing...')
#
# myDefaultDict = defaultdict(int)
#
# # Other packages and modules within existing code can be imported
# import collections
# from utils import dates, path
# myDate = dates.getDate(2020, 10, 23)
# print(myDate)
# #
# # # Import files paths - Python searches in the following order
# # # 1) builtins
# # # 2) current working directory
# # # 3) any directories that have been added to your system's "path"
# myList = list([1, 2, 3])  # list is found in builtins
# myDate = dates.getDate(2021, 4, 19)  # utils is found in the current working directory
# myDefaultDict = collections.defaultdict(int)  # collections is found in the Library path which is on the system's path
# # badFunc(9)  # This isn't found anywhere
# #
# path.printSystemPaths(__file__)
# print(f'Path for collections is {collections.__file__}')
# print(f'Path for dates is {dates.__file__}')
