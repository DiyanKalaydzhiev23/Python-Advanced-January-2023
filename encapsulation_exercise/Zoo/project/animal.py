class Animal:
    def __init__(self, name: str, gender: str, age: int, money_for_care: float):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
