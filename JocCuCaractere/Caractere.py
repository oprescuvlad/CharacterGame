from Entity import Entity

class Character(Entity) :
    def __init__(self,name:str , hp:int , attack:int ):
        super().__init__(name, attack)
        self.hp = hp
        self.weapon = None

    def afiseaza_specificatii(self):  #we print the type of weapon and the characteristics
        print(f'Character name : {self.name}')
        print("Power :", self.attack)
        print("Health points : ", self.hp)
        if self.weapon:
            print("Weapon: ", self.weapon.name)

    def receive_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")

