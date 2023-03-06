from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS: int = 50
    PRICE: float = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
