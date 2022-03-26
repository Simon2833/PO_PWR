import random


# Class where all the repeated math functions are grouped up in one place
class math:

    @staticmethod
    def randomPos(x, y):
        # Will be used to get coordinates of objects before creating for simplicity if current place would be occupied
        x = random.randint(0, x-1)
        y = random.randint(0, y-1)
        tab = [x, y]
        return tab
