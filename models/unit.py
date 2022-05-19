from abc import ABC, abstractmethod


# Basic villager class from whom every other citizen class is inherited
class unit(ABC):

    def __init__(self, cox, coy):
        self.cox = cox
        self.coy = coy


