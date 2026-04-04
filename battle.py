class DamageEvent:
    def __init__(self, attacker, defender, damage):
        self.attacker = attacker
        self.defender = defender
        self.damage = damage

class AttackProcessor:
    def attack(self, attacker, defender):
        damage = attacker.attack_enemy
        event = DamageEvent(attacker, defender, damage)
        defender.take_damage(event.damage)

        for effect in defender.effects:
            effect.on_damage(event)


