import math


class CrabCollection:
    def __init__(self):
        # list of crabs horizontal positions
        self.crabs = []

    def brute_force_find(self):
        target = 0
        cost = 0
        last_cost = 0

        while last_cost == 0 or cost < last_cost:
            for crab_position in self.crabs:
                single_cost = abs(target - crab_position)
                cost += single_cost

            if last_cost != 0 and cost > last_cost:
                return last_cost

            last_cost = cost
            cost = 0
            target += 1

        return cost
