class Effect():
    def __init__(self, owner):
        self.owner = owner
        self.active = True
    def react(self, event_type, event):
        if not self.active:
            return
        method_name = f"on_{event_type.value}"
        method = getattr(self, method_name, None)
        if method:
            method(event)
class Poison(Effect):
    def on_after_damage(self, event):
        if self.owner == event.attacker and event.damage > 0:
            event.defender.hp = 0
            self.active = False
        if self.owner == event.defender and event.counter_damage > 0:
            event.attacker.hp = 0
            self.active = False
class DivineShield(Effect):
    def on_before_damage(self, event):
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
