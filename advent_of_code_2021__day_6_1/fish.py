class Fish:
    FIRST_BIRTH_TIMER = 9
    OTHER_BIRTHS_TIMER = 7

    def __init__(self):
        self.first_birth = True
        self.time_to_birth = Fish.FIRST_BIRTH_TIMER

    def create_child(self):
        if self.time_to_birth == 0:
            self.first_birth = False
            self.time_to_birth = Fish.OTHER_BIRTHS_TIMER

            return Fish()
        else:
            return None

    def tick(self):
        self.time_to_birth -= 1

    @staticmethod
    def create_from_template(time_to_birth: int):
        fish = Fish()

        fish.time_to_birth = time_to_birth
        fish.first_birth = False

        return fish
