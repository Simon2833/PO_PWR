from abc import abstractmethod
from models.unit import unit


# Basic villager class from whom every other citizen class is inherited
class unitDynamic(unit):

    def __init__(self, cox, coy, id, maxhp, attack, armor, range):
        super().__init__(cox, coy)
        self.id = id
        self.maxhp = maxhp
        self.attack = attack
        self.armor = armor
        self.range = range
        self.cox = cox
        self.coy = coy



