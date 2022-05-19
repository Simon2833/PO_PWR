from models.unitDynamic import unitDynamic
from abc import abstractmethod


# One of three tribe classes which will be concluded in simulation
class archer(unitDynamic):

    def __init__(self, cox, coy, id, tribe, maxhp=100, attack=15, armor=0, range=4):
        super().__init__(cox, coy, id, maxhp, attack, armor, range)
        self.currenthp = maxhp
        self.tribe = tribe
        self.type = "villager"



