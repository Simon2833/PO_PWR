from models.resource import resource
from models.board import board
import unittest


class testResource(unittest.TestCase):

    def setUp(self):
        self.map = board(100, 100)
        self.tab = self.map.boardInit()
        self.tab = self.map.boardGenerate(self.tab, 0, 0, 0, 0)

    def testSpawnRate(self):
        startLen = len(resource.resourceList)
        resource.spawnRate(self.tab)
        assert(len(resource.resourceList) > startLen)
