from models.unitStatic import unitStatic
import models


# Food that can help tribe survive and is used to make new citizens
class resource(unitStatic):

    # List of food used in board class to store objects in their categories
    resourceList = []

    def __init__(self, cox, coy, id):
        super().__init__(cox, coy, id)

    def deletion(self, tribe, list, tab):
        tab[self.coy][self.cox] = 0
        del list[self.id]
        for food in range(len(list)):
            list[food].id = food
        tribe.morale = tribe.morale + 20

    @classmethod
    def spawnRate(cls, tab):
        pos = models.calc.randomPos(len(tab[0]), len(tab))
        while(tab[pos[1]][pos[0]] != 0):
            pos = models.calc.randomPos(len(tab[0]), len(tab))
        tab[pos[1]][pos[0]] = 1
        resource.resourceList.append(resource(pos[0], pos[1], len(resource.resourceList)))
