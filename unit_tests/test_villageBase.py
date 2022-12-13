from models.villageBase import villageBase
from models.board import board
import unittest


class testBoard(unittest.TestCase):

    def setUp(self):
        self.map = board(13, 45)
        self.tab = self.map.boardInit()
        self.tab = self.map.boardGenerate(self.tab, 1, 2, 3, 3)

    def testMoraleUpdate(self):
        villageBase.baseList[0].morale = 123
        villageBase.baseList[1].morale = 0

        villageBase.baseList[0].moraleUpdate("None", villageBase.baseList, self.tab)
        villageBase.baseList[1].moraleUpdate("None", villageBase.baseList, self.tab)
        assert(villageBase.baseList[1].morale == 40 and len(villageBase.baseList[1].populationList) == 2)
        assert(villageBase.baseList[0].morale == 50 and len(villageBase.baseList[0].populationList) == 4)

    def testGlobalWarAndGlobalPeace(self):
        villageBase.year1939()
        for base in villageBase.baseList:
            assert(base.status == "war")

        villageBase.christmasTruce()
        for base in villageBase.baseList:
            assert(base.status == "peace")