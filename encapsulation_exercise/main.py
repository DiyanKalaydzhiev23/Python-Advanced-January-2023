class Person:

    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self._age = age
        self.__height = height

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError

        self.__name = value


person = Person("diyan", 19, 1.90)
print(person._Person__height)

person.name = "Sasho"