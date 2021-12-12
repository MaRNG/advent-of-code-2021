import os
from submarine import Submarine


def process_real_commands():
    with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as f:
        lines = f.readlines()

        submarine = Submarine()
        submarine.submarine_navigation.process_commands(lines)

        print(submarine.get_multiplied_coordinates())


process_real_commands()
