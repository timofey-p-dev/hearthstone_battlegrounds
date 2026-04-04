from abc import ABC, abstractmethod
import random

class Hero(ABC):
    def __init__(self):
        self.hp = 30
        self.armor = 0
    
    @property
    @abstractmethod
    def name(self):       pass

    @property
    @abstractmethod
    def attack_enemy(self):     pass
    
    @abstractmethod
    def attack(self, other):      pass
        
    def take_damage(self, dmg):
        if dmg <= self.armor:
            self.armor -= dmg
        else: 
            self.hp = max(self.hp-(dmg-self.armor), 0)
            self.armor = 0

class Mag(Hero):
    def __init__(self):
        super().__init__()
        self.armor = 0

    @property
    def name(self):
        return 'Маг'
    
    @property
    def attack_enemy(self):
        return random.choices([3, 4], weights=[65, 35], k=1)[0]

    def attack(self, other):
        dmg = random.choices([3, 4], weights=[65, 35], k=1)[0]

        print(self.name, 'атакует', other.name, 'с возрождением')
        other.take_damage(dmg)

        if self.hp + dmg <= 30:
            self.hp += dmg
        else:
            self.hp = 30

        print('У', other.name, 'осталось', other.hp, 'HP')
        print(self.name, 'похилился на', dmg, 'HP')

class Tank(Hero):
    def __init__(self):
        super().__init__()
        self.armor = 10

    @property
    def name(self):
        return 'Танк'
    
    @property
    def attack_enemy(self):
        return random.choices([1, 5], weights=[50, 50], k=1)[0]

    def attack(self, other):
        dmg = random.choices([3, 4], weights=[50, 50], k=1)[0]
        print(self.name, 'отправляет снаряд в', other.name, 'с атакой', dmg)
        other.take_damage(dmg)
        print('У', other.name, 'осталось', other.hp, 'HP')

class Assassin(Hero):
    def __init__(self):
        super().__init__()
        self.armor = 2

    @property
    def name(self):
        return 'Ассасин'
    
    @property
    def attack_enemy(self):
        return random.choices([5, 6], weights=[50, 50], k=1)[0]

    def attack(self, other):
        dmg = random.choices([4, 5, 6], weights=[1, 3, 1], k=1)[0]
        print(self.name, 'атакует', other.name, 'с атакой', dmg)
        other.take_damage(dmg)
        print('У', other.name, 'осталось', other.hp, 'HP')

class Archer(Hero):
    def __init__(self):
        super().__init__()
        self.armor = 7

    @property
    def name(self):
        return 'Лучник'
    
    @property
    def attack_enemy(self):
        return random.choices([5, 3], weights=[40, 60], k=1)[0]

    def attack(self, other):
        dmg = random.choices([2, 3, 4, 5], weights=[20, 30, 30, 20], k=1)[0]
        print(self.name, 'атакует', other.name, 'с атакой', dmg)
        other.take_damage(dmg)
        print('У', other.name, 'осталось', other.hp, 'HP')




class IceMag(Mag): 
    @property
    def name(self):
        return 'Ледяной маг'
    
class FireMag(Mag):
    @property
    def name(self):
        return 'Огненный маг'
    
class TT(Tank):
    @property
    def name(self):
        return 'Тяжелый Танк'
class CT(Tank):
    @property
    def name(self):
        return 'Средний Танк'
    
class PersianAssassin(Assassin):
    @property
    def name(self):
        return 'Персидский Ассасин'
class SyiranAssassin(Assassin):
    @property
    def name(self):
        return 'Сирийский Ассасин'
    
class BlueArcher(Archer):
    @property
    def name(self):
        return 'Голубой лучник'
class RedArcher(Archer):
    @property
    def name(self):
        return 'Красный лучник'
    