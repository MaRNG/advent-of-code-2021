import unittest
import measurement


class TestMeasurement(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(measurement.measure_depth_increasing([]), 0)

    def test_example_challenge(self):
        example_data = [199,
                        200,
                        208,
                        210,
                        200,
                        207,
                        240,
                        269,
                        260,
                        263]

        self.assertEqual(measurement.measure_depth_increasing(example_data), 5)

#    def test_real_data_challenge(self):
#        self.assertEqual(measurement.measure_real_data(), 1722)


if __name__ == '__main__':
    unittest.main()
