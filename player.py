from hero import *

class Player:

    def __init__(self, nickname, hero):
        self.nickname = nickname
        self.hero = hero()

    def attack(self, other):
        self.hero.attack(other.hero)
        self.hero.take_damage(other.hero.attack_enemy)