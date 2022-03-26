from models.math import math
import random
import unittest


class test_random_pos(unittest.TestCase):

    def test_return_correct_tab(self):
        width = random.randint(1, 1000)
        height = random.randint(1, 1000)
        tab = math.random_pos(width, height)
        assert (0 <= tab[0] < 1000)
        assert (0 <= tab[1] < 1000)
