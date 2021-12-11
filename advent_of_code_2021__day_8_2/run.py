from seven_segment_display_decoder import SeventSegmentDisplayDecoder
import os


def run():
    with open(os.path.join(os.path.dirname(__file__), './data/input.txt'), 'r') as f:
        lines = f.readlines()

        count = 0

        for line in lines:
            split_line = line.strip().split(' | ', 2)

            key = split_line[0]
            output = split_line[1]

            decoder = SeventSegmentDisplayDecoder(key)

            count += int(decoder.decode_row(output))

        print(count)


run()
