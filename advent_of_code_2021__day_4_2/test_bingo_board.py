import unittest
from bingo_board import BingoBoard, BingoBoardPlace


class TestBingoBoard(unittest.TestCase):
    def test_init(self):
        data = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]

        bingo_board = BingoBoard(data)

        self.assertIsInstance(bingo_board.data[0][0], BingoBoardPlace)

    def test_chose_number(self):
        data = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 5, 8]
        ]

        bingo_board = BingoBoard(data)
        bingo_board.choose_number(5)

        self.assertEqual(bingo_board.chosen_numbers[0], 5)
        self.assertEqual(bingo_board.data[1][2].selected, True)
        self.assertEqual(bingo_board.data[2][1].selected, True)

    def test_finish_bingo(self):
        data = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 5, 8]
        ]

        bingo_board = BingoBoard(data)
        bingo_board.choose_number(5)
        bingo_board.choose_number(2)
        bingo_board.choose_number(1)
        bingo_board.choose_number(8)

        self.assertEqual(bingo_board.sum_unmarked_numbers(), 13)
        self.assertEqual(bingo_board.result, 104)

    def test_bingo_example_data(self):
        numbers_to_chose = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3,
                            26, 1]

        boards_data = [
            [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19]
            ],
            [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6]
            ],
            [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7]
            ]
        ]

        boards = []

        for board_data in boards_data:
            boards.append(BingoBoard(board_data))

        last_board_won: BingoBoard

        for number_to_chose in numbers_to_chose:
            for board in boards:
                if board.result == -1:
                    board.choose_number(number_to_chose)

                    if board.result != -1:
                        # self.assertEqual(board.result, 1924)
                        last_board_won = board

        self.assertEqual(last_board_won.result, 1924)

if __name__ == '__main__':
    unittest.main()
