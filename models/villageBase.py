from models.calc import calc
from models.unitStatic import unitStatic


# Main village base that will delete clan if destroyed
class villageBase(unitStatic):

    x = calc.yesOrNo()
    baseList = []

    def __init__(self, cox, coy, id, morale=50):
        super().__init__(cox, coy, id)
        self.food = 50
        self.status = "peace"
        self.maxhp = 100
        self.currenthp = 100
        self.population = 3
        self.populationList = []
        self.attitude = self.x
        self.morale = morale
