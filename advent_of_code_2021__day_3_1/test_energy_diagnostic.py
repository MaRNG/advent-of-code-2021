import unittest
from energy_diagnostic import EnergyDiagnostic


class TestEnergyDiagnostic(unittest.TestCase):
    def setUp(self) -> None:
        self.energy_diagnostic = EnergyDiagnostic()

    def test_process_log(self):
        self.energy_diagnostic.load_log([
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

        self.energy_diagnostic.process_log()

        self.assertEqual(self.energy_diagnostic.most_common_bits, ['1', '0', '1', '1', '0'])
        self.assertEqual(self.energy_diagnostic.least_common_bits, ['0', '1', '0', '0', '1'])

    def test_gamma_rate(self):
        self.energy_diagnostic.load_log([
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

        self.energy_diagnostic.process_log()

        self.assertEqual(self.energy_diagnostic.get_gamma_rate(), 22)

    def test_epsilon_rate(self):
        self.energy_diagnostic.load_log([
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

        self.energy_diagnostic.process_log()

        self.assertEqual(self.energy_diagnostic.get_epsilon_rate(), 9)

    def test_energy_consumption(self):
        self.energy_diagnostic.load_log([
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

        self.energy_diagnostic.process_log()

        self.assertEqual(self.energy_diagnostic.get_energy_consumption(), 198)


if __name__ == '__main__':
    unittest.main()
