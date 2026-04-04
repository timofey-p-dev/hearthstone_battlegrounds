class Hero():
    def __init__(self, name, hp, attack, armor, effects):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.effects = effects

    def take_damage(self, dmg):
        if dmg <= self.armor:
            self.armor -= dmg
        else: 
            self.hp = max(self.hp-(dmg-self.armor), 0)
            self.armor = 0
    