from models.village_base import village_base


# Basic villager class from whom every other citizen class is inherited
class villager:

    def __init__(self, id, maxhp, armor, tribe, attack, range, cox, coy):
        self.id = id
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.armor = armor
        self.tribe = tribe
        self.attack = attack
        self.range = range
        self.cox = cox
        self.coy = coy
