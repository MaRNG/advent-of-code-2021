import os
from swarm import Swarm


def run():
    with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as f:
        lines = f.readlines()

        fishes_to_create = [int(fish_timer) for fish_timer in lines[0].split(',')]

        swarm = Swarm.create_swarm_fishes_from_template(fishes_to_create)

        for i in range(0, 80):
            swarm.tick()

        print(len(swarm.fishes))


run()
