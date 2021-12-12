class BingoBoardPlace:
    def __init__(self, number: int):
        self.number = number
        self.selected: bool = False


class BingoBoard:
    # 5x5 grid
    # data must include rows and columns -> [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    def __init__(self, data: []):
        self.data = []
        self.chosen_numbers = []
        self.result = -1
        self.bingo_width = 0

        for row in data:
            processed_row = []
            self.bingo_width += 1

            for col in row:
                processed_row.append(BingoBoardPlace(col))

            self.data.append(processed_row)

    def choose_number(self, number: int):
        self.chosen_numbers.append(number)

        for row in self.data:
            for col in row:
                if col.number == number:
                    col.selected = True

        self.check_bingo_life()

    def check_bingo_life(self):
        # check row
        for row in self.data:
            correct_values = 0
            for col in row:
                if col.selected:
                    correct_values += 1

            if correct_values == self.bingo_width:
                self.end_bingo()

        # check col
        for i in range(0, self.data[0].__len__()):
            column = []
            for row in self.data:
                column.append(row[i])

            correct_values = 0
            for place in column:
                if place.selected:
                    correct_values += 1

            if correct_values == self.bingo_width:
                self.end_bingo()

    def end_bingo(self):
        summed = self.sum_unmarked_numbers()
        last_chosen_number = self.chosen_numbers[-1]

        self.result = summed * last_chosen_number

    def sum_unmarked_numbers(self) -> int:
        output = 0

        for row in self.data:
            for col in row:
                if not col.selected:
                    output += col.number

        return output
