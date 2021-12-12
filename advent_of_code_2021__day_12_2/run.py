from path_finder import PathFinder
import os

'''

path_finder = PathFinder([
'start-A',
'start-b',
'A-c',
'A-b',
'b-d',
'A-end',
'b-end'
])

print(path_finder.find_all_possible_paths())
'''


def run():
    with open(os.path.join(os.path.dirname(__file__), './data/input'), 'r') as f:
        lines = f.readlines()

        path_finder = PathFinder(lines)

        print(path_finder.find_all_possible_paths())


run()

