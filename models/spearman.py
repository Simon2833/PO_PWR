from models.villager import villager


# One of three tribe classes which will be concluded in simulation
class spearman(villager):


    def __init__(self, id, tribe, cox, coy, maxhp=150, attack=25, armor=3, range=2):
        super().__init__(id, maxhp, armor, tribe, attack, cox, coy, range)
        self.currenthp = maxhp
