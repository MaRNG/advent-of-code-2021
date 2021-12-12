from fish import Fish
import typing


class Swarm:
    def __init__(self):
        self.fishes: typing.List[Fish] = []

    def tick(self):
        current_fishes = self.fishes

        for fish in current_fishes:
            created_fish = fish.create_child()

            fish.tick()

            if created_fish is not None:
                self.fishes.append(created_fish)

    @staticmethod
    def create_swarm_fishes_from_template(fish_timers: [int]):
        swarm = Swarm()

        for fish_timer in fish_timers:
            swarm.fishes.append(Fish.create_from_template(fish_timer))

        return swarm
