import random
import math
import models


# Class where all the repeated calc functions are grouped up in one place
class calc:

    @classmethod
    def randomPos(cls, x, y):
        # Will be used to get coordinates of objects before creating for simplicity if current place would be occupied
        x = random.randint(0, x-1)
        y = random.randint(0, y-1)
        tab = [x, y]
        return tab

    @classmethod
    def yesOrNo(cls):
        # Help to randomize choosing between two things, for example if tribe is aggressive or not
        x = random.randint(0, 1)
        if x == 1:
            return True
        else:
            return False

    @classmethod
    def rangeBetween(cls, firstx, firsty, secondx, secondy):
        # Finds a distance between two locations
        x = abs(firstx - secondx)
        y = abs(firsty - secondy)

        answer = pow(x, 2) + pow(y, 2)
        answer = int(math.sqrt(answer))

        return answer

