from models.unitDynamic import unitDynamic


# One of three tribe classes which will be concluded in simulation
class warrior(unitDynamic):

    def __init__(self, cox, coy, id, tribe, maxhp=200, attack=40, armor=5, range=1):
        super().__init__(cox, coy, id, maxhp, attack, armor, range)
        self.currenthp = maxhp
        self.tribe = tribe
        self.type = "villager"
        self.job = "warrior"


