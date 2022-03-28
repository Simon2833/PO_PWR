import random
import math


# Class where all the repeated calc functions are grouped up in one place
class calc:

    @staticmethod
    def randomPos(x, y):
        # Will be used to get coordinates of objects before creating for simplicity if current place would be occupied
        x = random.randint(0, x-1)
        y = random.randint(0, y-1)
        tab = [x, y]
        return tab

    @staticmethod
    def yesOrNo():
        x = random.randint(0, 1)
        if x == 1:
            return True
        else:
            return False

    @staticmethod
    def range(firstx, firsty, secondx, secondy):
        x = abs(firstx - secondx)
        y = abs(firsty - secondy)

        answer = pow(x, 2) + pow(y, 2)
        answer = math.sqrt(answer)

        return answer
