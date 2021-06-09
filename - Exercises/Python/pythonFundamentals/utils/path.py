import os
import sys

def printSystemPaths(file):
    currentFilePath = os.path.dirname(os.path.realpath(file))
    print('------------------------------')
    print('Current paths are:')
    for path in set(sys.path):
        if '.egg' not in path and '.zip' not in path:
            if path == currentFilePath:
                print(f'**{path}**')
            else:
                print(path)
    print('------------------------------')