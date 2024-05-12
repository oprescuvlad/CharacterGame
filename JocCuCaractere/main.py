from Caractere import Character
from Arme import Arma

hero = Character('Hero' , 100 , 5)
enemy = Character('Enemy' , 100 , 5)
hero.weapon = Arma('Excalibur', 25, 'sword')
enemy.weapon = Arma('Wizard Staff', 15, 'mage')

print("Hero's specifications:")
hero.afiseaza_specificatii()
print()

print("Enemy's specifications:")
enemy.afiseaza_specificatii()
print()

while hero.hp > 0 and enemy.hp>0 :
    print(f"{hero.name} attacks {enemy.name} with {hero.weapon.name}!")
    enemy.receive_damage(hero.attack + hero.weapon.attack)
    print(f'{hero.name} has {hero.hp} and {enemy.name} has {enemy.hp}')
    if enemy.hp >= 0:
        print('The fight continues ')
    if enemy.hp <= 0:
        print(f'{enemy.name} has been defeated')
        break

    print(f"{enemy.name} attacks {hero.name} with {enemy.weapon.name}!")
    hero.receive_damage(enemy.attack + enemy.weapon.attack)
    print(f'{hero.name} has {hero.hp} and {enemy.name} has {enemy.hp}')
    if hero.hp >= 0:
        print('The fight continues ')
    if hero.hp <= 0:
        print(f'{hero.name} has been defeated')
        break

print(f"Your character's remaining HP: {hero.hp}")


