from abc import abstractmethod
from models.unit import unit


# Basic villager class from whom every other citizen class is inherited
class unitStatic(unit):

    def __init__(self, cox, coy, id):
        super().__init__(cox, coy, id)


