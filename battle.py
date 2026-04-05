from event_type import EventType
class DamageEvent:
    def __init__(self, attacker, defender, damage):
        self.attacker = attacker
        self.defender = defender
        self.damage = damage
        self.counter_damage = defender.attack

class AttackProcessor:
    def notify(self, heroes, event_type, event):
        for hero in heroes:
            hero.handle_event(event_type, event)
            
    def attack(self, attacker, defender):
        event = DamageEvent(attacker, defender, attacker.attack)
        heroes = [attacker, defender]

        self.notify(heroes, EventType.BEFORE_DAMAGE, event)

        defender.take_damage(event.damage)
        attacker.take_damage(event.counter_damage)

        self.notify(heroes, EventType.AFTER_DAMAGE, event)
