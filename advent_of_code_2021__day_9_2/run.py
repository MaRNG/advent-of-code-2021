from grid import Grid
import os

def run():
    with open(os.path.join(os.path.dirname(__file__), './data/input.txt'), 'r') as f:
        lines = f.readlines()

        grid = Grid.parse_raw_data(lines)

        print(grid.find_three_largest_basins())


run()

'''
grid = Grid.parse_raw_data([
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678'
])

print(grid.find_three_largest_basins())
'''
