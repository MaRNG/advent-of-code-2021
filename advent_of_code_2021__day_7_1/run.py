import os
from crab_collection import CrabCollection


def run():
    with open(os.path.join(os.path.dirname(__file__), './data/input.txt'), 'r') as f:
        lines = f.readlines()

        crab_positions = [int(fish_timer) for fish_timer in lines[0].split(',')]

        crab_collection = CrabCollection()

        for crab_position in crab_positions:
            crab_collection.crabs.append(crab_position)

        print(crab_collection.brute_force_find())


run()
