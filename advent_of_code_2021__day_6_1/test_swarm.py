import unittest
from swarm import Swarm


class TestSwarm(unittest.TestCase):
    def test_create_swarm_from_template(self):
        swarm = Swarm.create_swarm_fishes_from_template([
            3, 4, 3, 1, 2
        ])

        self.assertEqual(len(swarm.fishes), 5)
        self.assertEqual(swarm.fishes[0].time_to_birth, 3)
        self.assertEqual(swarm.fishes[0].first_birth, False)

    def test_example(self):
        swarm = Swarm.create_swarm_fishes_from_template([
            3, 4, 3, 1, 2
        ])

        # tick for 80 days
        for i in range(0, 80):
            swarm.tick()

        self.assertEqual(len(swarm.fishes), 5934)


if __name__ == '__main__':
    unittest.main()
