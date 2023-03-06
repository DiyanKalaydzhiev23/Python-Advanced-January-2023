from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS: int = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, Salmon.GRAMS)
