from models.villager import villager


# One of three tribe classes which will be concluded in simulation
class warrior(villager):

    # Variable 'tochange' will be changed when we decide what stats this class should have
    tochange = 3

    def __init__(self, id, tribe, cox, coy, maxhp=200, attack=40, armor=5, range=1):
        super().__init__(id, maxhp, armor, tribe, attack, cox, coy, range)
        self.currenthp = maxhp
