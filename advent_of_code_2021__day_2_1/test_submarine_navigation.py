import unittest
from submarine import Submarine


class SubmarineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.submarine = Submarine()

    def test_forward(self):
        self.submarine.submarine_navigation.process_command('forward 5')
        self.assertEqual(self.submarine.horizontal_position, 5)

    def test_up(self):
        self.submarine.submarine_navigation.process_command('up 5')
        self.assertEqual(self.submarine.vertical_position, -5)

    def test_down(self):
        self.submarine.submarine_navigation.process_command('down 5')
        self.assertEqual(self.submarine.vertical_position, 5)

    def test_example_challenge(self):
        commands = [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2'
        ]

        self.submarine.submarine_navigation.process_commands(commands)
        self.assertEqual(self.submarine.get_multiplied_coordinates(), 150)


if __name__ == '__main__':
    unittest.main()
