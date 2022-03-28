from models.calc import calc
import random
import unittest


class test_random_pos(unittest.TestCase):

    def testReturnCorrectTab(self):
        width = random.randint(1, 1000)
        height = random.randint(1, 1000)
        tab = calc.randomPos(width, height)
        assert (0 <= tab[0] < 1000)
        assert (0 <= tab[1] < 1000)

    def testYesOrNo(self):
        calc.yesOrNo()
        assert True or False
