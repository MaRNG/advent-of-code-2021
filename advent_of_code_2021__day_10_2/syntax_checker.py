import math


class SyntaxChecker:
    MAP = {
        '{': '}',
        '(' : ')',
        '[': ']',
        '<': '>'
    }

    SCORE = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def __init__(self, lines: [str]):
        self.lines = [line.strip() for line in lines]

    def check_lines(self) -> int:
        scores = []

        for line in self.lines:
            if not self.is_line_corrupted(line):
                scores.append(self.get_incomplete_line_score(line))

        return sorted(scores)[len(scores) // 2]

    def get_incomplete_line_score(self, line: str) -> int:
        all_brackets = []
        expected_brackets = []

        for bracket in line:
            if bracket in SyntaxChecker.MAP:
                all_brackets.append(bracket)
                expected_brackets.append(SyntaxChecker.MAP[bracket])
            else:
                expected_bracket = expected_brackets.pop()

                if expected_bracket == bracket:
                    all_brackets.pop()

        score = 0

        while len(expected_brackets) > 0:
            closing_bracket = expected_brackets.pop()

            score *= 5

            score += SyntaxChecker.SCORE[closing_bracket]

        return score

    def is_line_corrupted(self, line: str) -> bool:
        all_brackets = []
        expected_brackets = []

        for bracket in line:
            if bracket in SyntaxChecker.MAP:
                all_brackets.append(bracket)
                expected_brackets.append(SyntaxChecker.MAP[bracket])
            else:
                expected_bracket = expected_brackets.pop()

                if expected_bracket == bracket:
                    all_brackets.pop()
                else:
                    return True

        return False
