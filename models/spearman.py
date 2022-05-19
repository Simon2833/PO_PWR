from models.unitDynamic import unitDynamic


# One of three tribe classes which will be concluded in simulation
class spearman(unitDynamic):

    def __init__(self, cox, coy, id, tribe, maxhp=150, armor=3, range=2, attack=2):
        super().__init__(cox, coy, id, maxhp, attack, armor, range)
        self.currenthp = maxhp
        self.tribe = tribe
        self.type = "villager"

