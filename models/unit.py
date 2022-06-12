from abc import ABC, abstractmethod


# Basic abstract class from whom every other unit class is inherited
class unit(ABC):

    def __init__(self, cox, coy, id):
        self.cox = cox
        self.coy = coy
        self.id = id

    @abstractmethod
    def deletion(self, tribe, list, tab):
        pass

    @abstractmethod
    def heal(self):
        pass
