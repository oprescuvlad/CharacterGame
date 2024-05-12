from Entity import Entity

class Arma (Entity) :
    def __init__(self, name:str ,attack:int ,weapon_tipe:str):
        super().__init__(name, attack)
        self.weapon_tipe = weapon_tipe


    def afiseaza_specificatii(self):  #we print the type of weapon and the characteristics
        print(f'Weapond name : {self.name}')
        print("Power :", self.attack)
        print("Weapon tipe: ", self.weapon_tipe)

    def upgrade_weapon(self, bonus): #
        self.attack += bonus
        print("Weapon upgraded, the new power is : ", self.attack)

