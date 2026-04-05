class DamageEvent:
    def __init__(self, attacker, defender, damage):
        self.attacker = attacker
        self.defender = defender
        self.damage = damage
        self.counter_damage = defender.attack

class AttackProcessor:
    def attack(self, attacker, defender):
        event = DamageEvent(attacker, defender, attacker.attack)

        for hero in [attacker, defender]:
            for effect in hero.effects:
                effect.react('before_damage', event)

        defender.take_damage(event.damage)
        attacker.take_damage(event.counter_damage)

        for hero in [attacker, defender]:
            for effect in hero.effects:
                effect.react('after_damage', event)
