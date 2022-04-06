import models
import random
import unittest


class testBoard(unittest.TestCase):

    def setUp(self):
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.board = models.board(self.width, self.height)
        self.max = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
        self.maxPopulation = 3
        self.populationCount = (self.max[2] * self.maxPopulation)
        self.tab = self.board.boardInit()

    def testBoardInit(self):
        assert (len(self.tab)*len(self.tab[0]) == (self.width * self.height))
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                assert (self.tab[y][x] is None)

    def testFoodGenerate(self):
        count = 0
        self.board.foodGenerate(self.tab, self.max[0])
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] == 1):
                    count += 1
        assert (count == self.max[0])

    def testMonsterGenerate(self):
        count = 0
        self.board.monsterGenerate(self.tab, self.max[1])
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] == 2):
                    count += 1
        assert (count == self.max[1])

    def testVillagerGenerate(self):
        countVil = 0
        self.board.boardGenerate(self.tab, self.max[0], self.max[1], self.max[2])
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] in [4, 5, 6]):
                    countVil += 1

        print(countVil, self.populationCount, self.max[2], self.maxPopulation)
        assert (countVil == self.populationCount)

    def testTribeGenerate(self):
        count = 0
        self.board.tribeGenerate(self.tab, self.max[2])
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] == 3):
                    count += 1
        assert (count == self.max[2])

    def testIsNext(self):
        count = 0
        self.board.tribeGenerate(self.tab, self.max[2])
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] == 3):
                    count += 1

        for i in range(1, count):
            pos = [models.villageBase.baseList[i].cox, models.villageBase.baseList[i].coy]
            x = 0
            if(i == 1):
                if(models.calc.rangeBetween(models.villageBase.baseList[i-1].cox, models.villageBase.baseList[i-1].coy, pos[0], pos[1]) >= 3):
                    return True
            while (x != i):
                for j in range(1, i+1):
                    if(models.calc.rangeBetween(models.villageBase.baseList[i-j].cox, models.villageBase.baseList[i-j].coy, pos[0], pos[1]) >= 3):
                        x = x + 1
                if(x != i):
                    x = 0
                    pos = models.calc.randomPos(self.width, self.height)
            return True

    def testBoardGenerate(self):
        countOccupied = 0
        countEmpty = 0
        self.board.boardGenerate(self.tab, self.max[0], self.max[1], self.max[2])
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                if (self.tab[y][x] in [1, 2, 3, 4, 5, 6]):
                    countOccupied += 1
                else:
                    countEmpty += 1

        assert (countEmpty == (len(self.tab)*len(self.tab[0]))-countOccupied)
