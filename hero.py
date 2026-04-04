from abc import ABC, abstractmethod
import random

class Hero(ABC):
    def __init__(self):
        self.hp = 30
        self.armor = 0
        self.effects = []
    
    @property
    @abstractmethod
    def name(self):       pass

    @property
    @abstractmethod
    def attack_enemy(self):     pass
        
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
    