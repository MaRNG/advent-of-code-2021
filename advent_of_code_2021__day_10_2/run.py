from syntax_checker import SyntaxChecker
import os

'''

checker = SyntaxChecker([
    '{([(<{}[<>[]}>{[]{[(<()>',
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '(((({<>}<{<{<>}{[]{[]{}',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '<{([{{}}[<[[[<>{}]]]>[]]',
])

checker.check_lines()
'''


def run():
    with open(os.path.join(os.path.dirname(__file__), './data/input.txt'), 'r') as f:
        lines = f.readlines()

        syntax_checker = SyntaxChecker(lines)

        print(syntax_checker.check_lines())


run()
