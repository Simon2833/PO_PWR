from models.board import board

from unittest import TestCase, mock
import models

class testBoard(TestCase):


    def setUp(self):
        self.map = board(25, 75)
        self.tab = self.map.boardInit()

    def testBoardInit(self):
        tab = self.map.boardInit()
        assert(0 <= len(tab[0]) < 26)
        assert(0 <= len(tab) < 76)
        assert(tab[4][12] is None)

    def testBoardGenerate(self):
        tab = self.map.boardGenerate(self.tab, 2, 3, 4, 5)
        assert(tab[4][12] in [0, 1, 2, 3, 4, 5, 6])
        assert(tab[1][1] in [0, 1, 2, 3, 4, 5, 6])
        assert(tab[15][2] in [0, 1, 2, 3, 4, 5, 6])

    def testFoodGenerate(self):
        with mock.patch.object(self.map, "_board__foodGenerate") as food:
            self.map.boardGenerate(self.tab, 20, 3, 4, 5)
            food.assert_called_once_with(self.tab, 20)


