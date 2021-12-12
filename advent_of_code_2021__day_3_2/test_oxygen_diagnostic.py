import unittest
from oxygen_diagnostic import OxygenDiagnostic


class TestEnergyDiagnostic(unittest.TestCase):
    def setUp(self) -> None:
        self.oxygen_diagnostic = OxygenDiagnostic()

    def test_process_log(self):
        self.oxygen_diagnostic.load_log([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ])

        self.oxygen_diagnostic.process_log()

        self.assertEqual(self.oxygen_diagnostic.oxygen_generator_rating_binary_row, '10111')
        self.assertEqual(self.oxygen_diagnostic.co2_scrubber_rating_binary_row, '01010')

    def test_oxygen_generator_rating(self):
        self.oxygen_diagnostic.load_log([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ])

        self.oxygen_diagnostic.process_log()

        self.assertEqual(self.oxygen_diagnostic.get_oxygen_generator_rating(), 23)

    def test_co2_scrubber_rating(self):
        self.oxygen_diagnostic.load_log([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ])

        self.oxygen_diagnostic.process_log()

        self.assertEqual(self.oxygen_diagnostic.get_co2_scrubber_rating(), 10)

    def test_life_support_rating(self):
        self.oxygen_diagnostic.load_log([
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ])

        self.oxygen_diagnostic.process_log()

        self.assertEqual(self.oxygen_diagnostic.get_life_support_rating(), 230)


if __name__ == '__main__':
    unittest.main()
