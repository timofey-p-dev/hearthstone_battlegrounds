from battle import DamageEvent, AttackProcessor
from create_heroes import heroes

ap = AttackProcessor()
hero1 = heroes[0]  # Murloc
hero2 = heroes[1]  # Beast
print(f'Герой {hero1.name} атакует героя {hero2.name}')
print(f'До атаки: хп {hero1.name}: {hero1.hp}, Хп {hero2.name}: {hero2.hp}')
ap.attack(hero1, hero2)
print(f'После атаки: хп {hero1.name}: {hero1.hp}, Хп {hero2.name}: {hero2.hp}')

