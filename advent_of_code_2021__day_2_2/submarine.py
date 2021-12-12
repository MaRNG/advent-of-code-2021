class Submarine:
    def __init__(self):
        self.horizontal_position: int = 0

        # depth (inverse axis)
        self.vertical_position: int = 0

        self.aim: int = 0

        # navigation of submarine
        from submarine_navigation import SubmarineNavigation
        self.submarine_navigation = SubmarineNavigation(self)

    def forward(self, amount: int):
        self.horizontal_position += amount
        self.vertical_position += amount * self.aim

    def down(self, amount: int):
        self.aim += amount

    def up(self, amount: int):
        self.aim -= amount

    def get_multiplied_coordinates(self) -> int:
        return self.horizontal_position * self.vertical_position
