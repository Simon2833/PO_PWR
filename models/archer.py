from villager import villager

#archer class inherited from villager class
class archer(villager):
    def __init__(self, name, tribe, maxhp=tochange, attack=tochange, armor=tochange, morale=tochange):
        super().__init__(name, maxhp, armor, tribe, attack, morale)
        self.currenthp = maxhp

#variable 'tochange' will be changed when we decide what stats this class should have
tochange = 3