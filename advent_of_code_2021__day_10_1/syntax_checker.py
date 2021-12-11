class SyntaxChecker:
    MAP = {
        '{': '}',
        '(' : ')',
        '[': ']',
        '<': '>'
    }

    SCORE = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def __init__(self, lines: [str]):
        self.lines = [line.strip() for line in lines]

    def check_lines(self) -> int:
        output = 0

        for line in self.lines:
            output += self.check_line(line)

        return output

    def check_line(self, line: str) -> int:
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
                    return SyntaxChecker.SCORE[bracket]

        score = 0

        return score
