import enum


class MeasurementType(enum.Enum):
    OXYGEN_GENERATOR = 1,
    CO2_SCRUBBER = 2


class OxygenDiagnostic:
    def __init__(self):
        self.log: [] = []

        self.co2_scrubber_rating_binary_row: str = ''
        self.oxygen_generator_rating_binary_row: str = ''

    def load_log(self, log: [str]):
        self.log = log

    def process_log(self):
        # if log is not empty
        if self.log:
            self.co2_scrubber_rating_binary_row = self.process_stack(self.log, MeasurementType.CO2_SCRUBBER)
            self.oxygen_generator_rating_binary_row = self.process_stack(self.log, MeasurementType.OXYGEN_GENERATOR)

    # process stack recursively and return final binary row dependently on measurement type
    def process_stack(self, stack: [], measurement_type: MeasurementType, measurement_bit_index: int = 0) -> str:
        if stack.__len__() == 1:
            return stack[0]

        one_bit_count = 0
        zero_bit_count = 0

        for row in stack:
            if row[measurement_bit_index] == '0':
                zero_bit_count += 1
            else:
                one_bit_count += 1

        filtered_new_stack = []

        if measurement_type == MeasurementType.OXYGEN_GENERATOR:
            if one_bit_count >= zero_bit_count:
                for row in stack:
                    if row[measurement_bit_index] == '1':
                        filtered_new_stack.append(row)
            else:
                for row in stack:
                    if row[measurement_bit_index] == '0':
                        filtered_new_stack.append(row)
        else:
            if zero_bit_count <= one_bit_count:
                for row in stack:
                    if row[measurement_bit_index] == '0':
                        filtered_new_stack.append(row)
            else:
                for row in stack:
                    if row[measurement_bit_index] == '1':
                        filtered_new_stack.append(row)

        return self.process_stack(filtered_new_stack, measurement_type, measurement_bit_index + 1)

    def get_co2_scrubber_rating(self) -> int:
        return int(self.co2_scrubber_rating_binary_row, 2)

    def get_oxygen_generator_rating(self) -> int:
        return int(self.oxygen_generator_rating_binary_row, 2)

    def get_life_support_rating(self) -> int:
        return self.get_co2_scrubber_rating() * self.get_oxygen_generator_rating()
