from submarine import Submarine


class SubmarineNavigation:
    def __init__(self, submarine_parent: Submarine):
        self.submarine_parent = submarine_parent

    def process_command(self, command: str):
        (direction, amount) = command.split(' ', 2)
        amount_number: int = int(amount)

        if direction == 'forward':
            self.submarine_parent.forward(amount_number)
        elif direction == 'down':
            self.submarine_parent.down(amount_number)
        elif direction == 'up':
            self.submarine_parent.up(amount_number)

    def process_commands(self, commands: []):
        for command in commands:
            self.process_command(command)
