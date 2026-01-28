import random


class Bug:
    def __init__(self, position=12):
        self.position = position

    def move(self):
        step = random.choice([-1, 1])
        self.position += step

        if self.position == 13:
            self.position = 1
        elif self.position == 0:
            self.position = 12

        return self.position
