from models.villager import Villager
#spearman class inherited from villager class
class spearman(Villager):

    #variable 'tochange' will be changed when we decide what stats this class should have
    tochange = 3
    
    def __init__(self, name, tribe, position, maxhp=tochange, attack=tochange, armor=tochange, morale=tochange, range=tochange):
        super().__init__(name, maxhp, armor, tribe, attack, morale, position, range)
        self.currenthp = maxhp


