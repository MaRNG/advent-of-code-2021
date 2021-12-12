import unittest
from vents_map import VentsMap


class TestVentsMap(unittest.TestCase):
    def test_add_vents(self):
        vents_map = VentsMap()

        vents_map.add_vent_coordinates((0, 0), (5, 0))

        self.assertEqual(vents_map.map, {
            '0,0': 1,
            '1,0': 1,
            '2,0': 1,
            '3,0': 1,
            '4,0': 1,
            '5,0': 1,
        })

    def test_add_diagonal_vents(self):
        vents_map = VentsMap()

        vents_map.add_vent_coordinates((9, 7), (7, 9))

        self.assertEqual(vents_map.map, {
            '9,7': 1,
            '8,8': 1,
            '7,9': 1,
        })

    def test_add_overlap_vents(self):
        vents_map = VentsMap()

        vents_map.add_vent_coordinates((0, 0), (5, 0))
        vents_map.add_vent_coordinates((2, 0), (7, 0))

        self.assertEqual(vents_map.map, {
            '0,0': 1,
            '1,0': 1,
            '2,0': 2,
            '3,0': 2,
            '4,0': 2,
            '5,0': 2,
            '6,0': 1,
            '7,0': 1,
        })

    def test_overlap_vents(self):
        vents_map = VentsMap()

        vents_map.add_vent_coordinates((0, 0), (5, 0))
        vents_map.add_vent_coordinates((0, 0), (5, 5))

        self.assertEqual(vents_map.get_overlapped_vents_count(), 1)

    def test_example(self):
        vents_map = VentsMap()

        vents_map.add_vent_coordinates((0, 9), (5, 9))
        vents_map.add_vent_coordinates((8, 0), (0, 8))
        vents_map.add_vent_coordinates((9, 4), (3, 4))
        vents_map.add_vent_coordinates((2, 2), (2, 1))
        vents_map.add_vent_coordinates((7, 0), (7, 4))
        vents_map.add_vent_coordinates((6, 4), (2, 0))
        vents_map.add_vent_coordinates((0, 9), (2, 9))
        vents_map.add_vent_coordinates((3, 4), (1, 4))
        vents_map.add_vent_coordinates((0, 0), (8, 8))
        vents_map.add_vent_coordinates((5, 5), (8, 2))

        self.assertEqual(vents_map.get_overlapped_vents_count(), 12)


if __name__ == '__main__':
    unittest.main()
