import unittest
from submarine import Submarine


class SubmarineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.submarine = Submarine()

    def test_forward(self):
        self.submarine.forward(5)

        self.assertEqual(self.submarine.horizontal_position, 5)

    def test_up(self):
        self.submarine.up(5)

        self.assertEqual(self.submarine.aim, -5)

    def test_down(self):
        self.submarine.down(5)

        self.assertEqual(self.submarine.aim, 5)

    def test_get_coordinates(self):
        self.submarine.down(5)
        self.submarine.forward(5)

        self.assertEqual(self.submarine.get_multiplied_coordinates(), 125)


if __name__ == '__main__':
    unittest.main()
