class SeventSegmentDisplayDecoder:
    def __init__(self, key: str):
        self.key = key
        self.decoded_numbers = {}

        self.decode_key()

    def decode_key(self):

        split_key = self.key.split(' ')

        # decode easiest numbers
        for one_key in self.key.split(' '):
            one_key_length = len(set(one_key))

            if one_key_length == 2:
                self.decoded_numbers[1] = set(one_key)
                split_key.remove(one_key)
            elif one_key_length == 3:
                self.decoded_numbers[7] = set(one_key)
                split_key.remove(one_key)
            elif one_key_length == 4:
                self.decoded_numbers[4] = set(one_key)
                split_key.remove(one_key)
            elif one_key_length == 7:
                self.decoded_numbers[8] = set(one_key)
                split_key.remove(one_key)

        # decode 3
        for one_key in split_key:
            one_key_length = len(set(one_key))

            if one_key_length == 5 and SeventSegmentDisplayDecoder._string_contains_characters(one_key, self.decoded_numbers[7]):
                self.decoded_numbers[3] = set(one_key)

        # decode 9
        for one_key in split_key:
            one_key_length = len(set(one_key))

            if one_key_length == 6 and SeventSegmentDisplayDecoder._string_contains_characters(one_key, self.decoded_numbers[3]):
                self.decoded_numbers[9] = set(one_key)

        # decode 0
        for one_key in split_key:
            one_key_length = len(set(one_key))

            if \
                    one_key_length == 6 \
                    and SeventSegmentDisplayDecoder._string_contains_characters(one_key, self.decoded_numbers[7])\
                    and set(one_key) != self.decoded_numbers[9]:
                self.decoded_numbers[0] = set(one_key)

        # decode 6
        for one_key in split_key:
            one_key_length = len(set(one_key))

            if one_key_length == 6 and set(one_key) != self.decoded_numbers[9] and set(one_key) != self.decoded_numbers[0]:
                self.decoded_numbers[6] = set(one_key)

        # decode 5
        for one_key in split_key:
            one_key_length = len(set(one_key))

            if one_key_length == 5 and SeventSegmentDisplayDecoder._string_missing_characters_count(one_key, self.decoded_numbers[6]) == 1 and set(one_key) != self.decoded_numbers[3]:
                self.decoded_numbers[5] = set(one_key)

        # decode 2
        for one_key in split_key:
            one_key_length = len(set(one_key))

            if one_key_length == 5 and set(one_key) != self.decoded_numbers[5] and set(one_key) != self.decoded_numbers[3]:
                self.decoded_numbers[2] = set(one_key)

    def decode_row(self, row: str) -> str:
        output = ''

        for encoded_number in row.split(' '):
            output += self.decode_number(encoded_number)

        return output

    def decode_number(self, encoded_number: str) -> str:
        for decoded_number_idx in self.decoded_numbers:
            if set(encoded_number) == self.decoded_numbers[decoded_number_idx]:
                return str(decoded_number_idx)

        return '-'

    @staticmethod
    def _string_contains_characters(haystack: str, characters: []):
        contains = True

        for character in characters:
            if character not in haystack:
                contains = False

        return contains

    @staticmethod
    def _string_missing_characters_count(haystack: str, characters: []) -> int:
        missing_count = 0

        for character in characters:
            if character not in haystack:
                missing_count += 1

        return missing_count
