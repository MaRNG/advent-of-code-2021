class Row:
    def __init__(self, row: str):
        self.row = row.strip()

    def get_output(self) -> str:
        return self.row.split(' | ', 2)[1]

    def get_numbers_count(self) -> int:
        output = 0

        encoded_numbers = self.get_output().split(' ')

        for encoded_number in encoded_numbers:
            encoded_number_length = len(set(encoded_number))

            if encoded_number_length == 2 or encoded_number_length == 3 or encoded_number_length == 4 or encoded_number_length == 7:
                output += 1

        return output
