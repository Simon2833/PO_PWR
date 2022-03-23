import random

class math:

    @staticmethod
    def random_pos(y, x):
        x = random.randint(0, x-1)
        y = random.randint(0, y-1)
        tab = [x, y]
        return tab