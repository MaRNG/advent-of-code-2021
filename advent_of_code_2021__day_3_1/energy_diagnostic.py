class EnergyDiagnostic:
    def __init__(self):
        self.log: [] = []

        self.most_common_bits: [str] = []
        self.least_common_bits: [str] = []

    def load_log(self, log: [str]):
        self.log = log

    def process_log(self):
        # if log is not empty
        if self.log:
            first_line: str = self.log[0]

            zero_bit_count: [] = []
            one_bit_count: [] = []

            for bit in first_line:
                zero_bit_count.append(0)
                one_bit_count.append(0)

            for binary_row in self.log:
                for bit_index, bit in enumerate(binary_row):
                    if bit == '0':
                        zero_bit_count[bit_index] += 1
                    elif bit == '1':
                        one_bit_count[bit_index] += 1

            for zero_bit_count_index, zero_bit_count in enumerate(zero_bit_count):
                if zero_bit_count > one_bit_count[zero_bit_count_index]:
                    self.most_common_bits.append('0')
                    self.least_common_bits.append('1')
                elif zero_bit_count < one_bit_count[zero_bit_count_index]:
                    self.most_common_bits.append('1')
                    self.least_common_bits.append('0')

    def get_gamma_rate(self) -> int:
        binary_row = ''.join(self.most_common_bits)
        return int(binary_row, 2)

    def get_epsilon_rate(self) -> int:
        binary_row = ''.join(self.least_common_bits)
        return int(binary_row, 2)

    def get_energy_consumption(self) -> int:
        return self.get_gamma_rate() * self.get_epsilon_rate()
