from models.calc import calc
from models.board import board
from models.monster import monster
import unittest


class test_random_pos(unittest.TestCase):

    def setUp(self):
        self.map = board(48, 32)
        self.tab = self.map.boardInit()
        self.tab = self.map.boardGenerate(self.tab, 1, 2, 3, 3)
        self.result = calc.randomPos(21, 37)

    def testRandomChance(self):
        for i in range(100000):
            result = calc.randomChance()
            assert(0 < result < 101)

    def testRandomPos(self):
        result = calc.randomPos(21, 37)
        assert(0 <= result[0] < 22)
        assert(0 <= result[1] < 38)

    def testMovePos(self):
        pos = [monster.monsterList[1].cox, monster.monsterList[1].coy]
        result = calc.movePos(self.tab, monster.monsterList[1], monster.monsterList)
        assert(self.tab[result[1]][result[0]] == 0 or result == pos)

    def testYesOrNo(self):
        result = calc.yesOrNo(23, 45)
        assert(result == 23 or result == 45)

    def testRangeBetween(self):
        result = calc.rangeBetween(5, 3, 8, 12)
        assert(result > 0)
        assert(result < 10)

