from grid import Grid
import os

'''
data = [
'5483143223',
'2745854711',
'5264556173',
'6141336146',
'6357385478',
'4167524645',
'2176841721',
'6882881134',
'4846848554',
'5283751526'
]

grid = Grid.create_from_lines(data)

for i in range(0, 100):
    grid.tick()

print(grid.flashes)
'''

def run():
    with open(os.path.join(os.path.dirname(__file__), './data/input'), 'r') as f:
        lines = f.readlines()

        grid = Grid.create_from_lines(lines)

        for i in range(0, 100):
            grid.tick()

        print(grid.flashes)


run()
