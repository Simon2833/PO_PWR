from models.unitStatic import unitStatic


# Food that can help tribe survive and is used to make new citizens
class resource(unitStatic):

    # List of food used in board class to store objects in their categories
    resourceList = []

    def __init__(self, cox, coy, id):
        super().__init__(cox, coy, id)
