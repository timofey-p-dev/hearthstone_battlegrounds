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
    
    def handle_event(self, event_type, event):
        for effect in self.effects[:]:
            effect.react(event_type, event)
        self.effects = [effect for effect in self.effects if effect.active]
    