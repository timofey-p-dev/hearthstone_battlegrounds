class PoisonEffect():
    def on_damage(self, event):
        event.defender.hp = 0
def create_effect(effect_name):
    mapping = {
        'poison': PoisonEffect
    }
    return [mapping.get(name)() for name in effect_name]