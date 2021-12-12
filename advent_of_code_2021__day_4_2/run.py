import os
from bingo_board import BingoBoard


def run():
    with open(os.path.join(os.path.dirname(__file__), 'data/input.txt'), 'r') as f:
        lines = f.readlines()

        # load numbers to choose in bingo
        values_to_choose = lines[0].split(',')

        # load bingo boards
        line = 1
        boards = []

        while line < lines.__len__():
            line += 1

            board_data = []

            for i in range(0, 5):

                board_data_row = []

                for number in lines[line].split(' '):
                    if number != '':
                        board_data_row.append(int(number.replace('\n', '')))

                board_data.append(board_data_row)

                line += 1

            boards.append(BingoBoard(board_data))

        last_board_won: BingoBoard

        for value_to_choose in values_to_choose:
            for board in boards:
                if board.result == -1:
                    board.choose_number(int(value_to_choose))

                    if board.result != -1:
                        last_board_won = board

        print(last_board_won.result)


run()
