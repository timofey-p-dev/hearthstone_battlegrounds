class Effect():
    def react(self, event_type, event):
        pass
class Poison(Effect):
    def __init__(self, owner):
        self.active = True
        self.owner = owner
    def react(self, event_type, event):
        if not self.active:
            return
        if event_type == 'after_damage':
            if self.owner == event.attacker and event.damage > 0:
                event.defender.hp = 0
                self.active = False
            if self.owner == event.defender and event.counter_damage > 0:
                event.attacker.hp = 0
                self.active = False
class DivineShield(Effect):
    def __init__(self, owner):
        self.active = True
        self.owner = owner
    def react(self, event_type, event):
        if not self.active:
            return
        if event_type == 'before_damage':
            if self.owner == event.defender:
                event.damage = 0
                self.active = False
            if self.owner == event.attacker:
                event.counter_damage = 0
                self.active = False

EFFECTS = {
    'poison': Poison,
    'divine_shield': DivineShield
}

def create_effect(name, owner):
    cls = EFFECTS.get(name)
    if cls is None:
        raise ValueError(f"Effect {name} not found")
    return cls(owner)
