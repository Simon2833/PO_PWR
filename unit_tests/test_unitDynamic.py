from models.unitDynamic import unitDynamic
from models.board import board
from models.monster import monster
from models.villageBase import villageBase
import unittest


class testBoard(unittest.TestCase):

    def setUp(self):
        self.map = board(13, 45)
        self.tab = self.map.boardInit()
        self.tab = self.map.boardGenerate(self.tab, 1, 2, 3, 3)

    def testMove(self):
        pos1 = [monster.monsterList[0].cox, monster.monsterList[0].coy]
        unitDynamic.move(self.tab, monster.monsterList[0], monster.monsterList)
        pos2 = [monster.monsterList[0].cox, monster.monsterList[0].coy]
        assert(self.tab[pos1[1]][pos1[0]] == 0 or self.tab[pos1[1]][pos1[0]] == 2)
        assert(self.tab[pos2[1]][pos2[0]] == 2)

    def testDeletionVillagers(self):
        pos = [villageBase.baseList[0].populationList[2].cox, villageBase.baseList[0].populationList[2].coy]
        moral = villageBase.baseList[0].morale
        leng = len(villageBase.baseList[0].populationList)
        villageBase.baseList[0].populationList[2].deletion("None", villageBase.baseList, self.tab)
        assert(leng > len(villageBase.baseList[0].populationList))
        assert(self.tab[pos[1]][pos[0]] == 0)
        assert(moral > villageBase.baseList[0].morale)

    def testDeletionMonster(self):
        pos = [monster.monsterList[1].cox, monster.monsterList[1].coy]
        leng = len(monster.monsterList)
        moral = villageBase.baseList[0].morale
        monster.monsterList[1].deletion(villageBase.baseList[0], monster.monsterList, self.tab)
        assert(leng > len(monster.monsterList))
        assert(moral < villageBase.baseList[0].morale)
        assert(self.tab[pos[1]][pos[0]] == 0)

    def testHeal(self):
        monster.monsterList[1].currenthp = 30
        hp1 = monster.monsterList[1].currenthp
        hp2 = monster.monsterList[0].currenthp
        monster.monsterList[1].heal()

        assert(monster.monsterList[1].currenthp > hp1)
        assert(monster.monsterList[0].currenthp == hp2)