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

        self.optimize_fishes()

    def optimize_fishes(self):
        optimized_fishes = {}

        for fish in self.fishes:
            if fish.time_to_birth in optimized_fishes:
                optimized_fishes[fish.time_to_birth].representing_fishes_count += fish.representing_fishes_count
            else:
                optimized_fishes[fish.time_to_birth] = fish

        for fish in self.fishes:
            if fish not in optimized_fishes.values():
                self.fishes.remove(fish)

    def get_fish_count(self) -> int:
        output = 0

        for fish in self.fishes:
            output += fish.representing_fishes_count

        return output

    @staticmethod
    def create_swarm_fishes_from_template(fish_timers: [int]):
        swarm = Swarm()

        optimized_fish_timers = {}

        for fish_timer in fish_timers:
            if fish_timer in optimized_fish_timers:
                optimized_fish_timers[fish_timer] += 1
            else:
                optimized_fish_timers[fish_timer] = 1

        for (i, optimized_fish_timer) in optimized_fish_timers.items():
            swarm.fishes.append(Fish.create_from_template(i, optimized_fish_timer))

        return swarm
