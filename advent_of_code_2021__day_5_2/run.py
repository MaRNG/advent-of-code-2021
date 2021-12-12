import os
from vents_map import VentsMap


def run():
    with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as f:
        lines = f.readlines()

        vents_map = VentsMap()

        for line in lines:
            coordinates = line.split(' -> ')

            raw_start = coordinates[0]
            raw_end = coordinates[1]

            start = [int(number) for number in raw_start.split(',')]
            end = [int(number) for number in raw_end.split(',')]

            vents_map.add_vent_coordinates((start[0], start[1]), (end[0], end[1]))

        print(vents_map.get_overlapped_vents_count())


run()
