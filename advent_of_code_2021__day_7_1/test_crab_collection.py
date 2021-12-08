import unittest
from crab_collection import CrabCollection


class TestCrabCollection(unittest.TestCase):
    def test_example(self):
        crab_collection = CrabCollection()

        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

        for number in data:
            crab_collection.crabs.append(number)

        self.assertEqual(crab_collection.brute_force_find(), 37)


if __name__ == '__main__':
    unittest.main()
