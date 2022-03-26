import models
import random
import unittest


class testBoard(unittest.TestCase):

    def setUp(self):
        self.width = random.randint(1, 100)
        self.height = random.randint(1, 100)
        self.board = models.board(self.width, self.height)
        self.max1 = random.randint(1, 50)
        self.max2 = random.randint(1, 50)
        self.tab = self.board.boardInit()

    def testBoardInit(self):

        assert (len(self.tab)*len(self.tab[0]) == (self.width * self.height))
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                assert (self.tab[y][x] is None)

    def testFoodGenerate(self):
        count = 0
        self.board.foodGenerate(self.tab, self.max1)
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] == 1):
                    count += 1
        assert (count == self.max1)

    def testMonsterGenerate(self):
        count = 0
        self.board.monsterGenerate(self.tab, self.max2)
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] == 2):
                    count += 1
        assert (count == self.max2)

    def testBoardGenerate(self):
        count1 = 0
        count2 = 0
        count3 = 0
        self.board.boardGenerate(self.tab, self.max1, self.max2)
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] == 1):
                    count1 += 1
                elif (self.tab[y][x] == 2):
                    count2 += 1
                else:
                    count3 += 1
        assert (count1 == self.max1)
        assert (count2 == self.max2)
        assert (count3 == (len(self.tab)*len(self.tab[0]))-(self.max1+self.max2))
