from models.villager import villager


# One of three tribe classes which will be concluded in simulation
class archer(villager):

    def __init__(self, id, tribe, cox, coy, maxhp=100, attack=15, armor=0, range=4):
        super().__init__(id, maxhp, armor, tribe, attack, cox, coy, range)
        self.currenthp = maxhp
