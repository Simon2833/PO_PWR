import models


#board class---------
class board:

    tab = []

    def __init__(self, cox, coy):
        self.cox = cox
        self.coy = coy


    def board_init(self):
        tab = [[None]*self.cox for _ in range(self.coy)]
        return tab




    def board_generate(self, tab, max_food):
        food_count = 0
        while(food_count != max_food):
            pos = models.math.random_pos(self.cox, self.coy)
            if(tab[pos[1]][pos[0]] != 1):
                tab[pos[1]][pos[0]] = 1
                models.resource.food_list.append(models.resource(pos[1], pos[0]))
                food_count += 1
        for y in range(len(tab)):
            print()
            for x in range(len(tab[y])):
                if(tab[y][x] != 1):
                    tab[y][x] = 0



                print(tab[y][x], end="|")

        return tab


#board initialization-------
'''print("How big the board should be?")
x = int(input("Please input width of the board: "))
y = int(input("Please input height of the board: "))
map = board(x, y)
print("x: " + str(map.wspx) + "\ny: "  + str(map.wspy))'''