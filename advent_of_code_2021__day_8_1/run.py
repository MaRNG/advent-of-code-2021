import os
from row import Row


def run():
    with open(os.path.join(os.path.dirname(__file__), './data/input.txt'), 'r') as f:
        lines = f.readlines()

        count = 0

        for line in lines:
            row = Row(line)

            count += row.get_numbers_count()

        print(count)


run()
