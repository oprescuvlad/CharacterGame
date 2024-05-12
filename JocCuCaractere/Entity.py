class Entity:
    def __init__(self, name: str, attack: int):
        self.name = name
        self.attack = attack

    def __str__(self):
        return f"Name: {self.name}, Attack: {self.attack}"