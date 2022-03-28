from models.calc import calc


# Main village base that will delete clan if destroyed
class village_base:

    x = calc.yesOrNo()
    baseList = []

    def __init__(self, cox, coy):
        self.food = 50
        self.status = "peace"
        self.maxhp = 100
        self.currenthp = 100
        self.cox = cox
        self.coy = coy
        self.id = len(self.baseList)
        self.population = 3
        self.populationList = []
        self.attitude = self.x
