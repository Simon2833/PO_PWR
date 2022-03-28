from models.villager import villager


# One of three tribe classes which will be concluded in simulation
class warrior(villager):

    # Variable 'tochange' will be changed when we decide what stats this class should have
    tochange = 3

    def __init__(self, tribe, cox, coy, name="Edzio", maxhp=tochange, attack=tochange, armor=tochange, morale=tochange, range=tochange):
        super().__init__(name, maxhp, armor, tribe, attack, morale, cox, coy, range)
        self.currenthp = maxhp
