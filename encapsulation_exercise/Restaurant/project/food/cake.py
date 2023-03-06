from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS: int = 250
    CALORIES: int = 1000
    PRICE: int = 5

    def __init__(self, name: str):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)


c = Cake("name")
print(c.price)