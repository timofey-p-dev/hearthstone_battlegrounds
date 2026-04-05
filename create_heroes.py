from effect_factory import create_effect
from hero import Hero

HERO_STATS = {
    'Murloc':       {'hp': 8, 'attack': 4, 'armor': 0, 'effects': ['poison']},
    'Beast':        {'hp': 8, 'attack': 8, 'armor': 0, 'effects': ['divine_shield']},
    'Demon':        {'hp': 20, 'attack': 3, 'armor': 0, 'effects': []},
    'Dragon':       {'hp': 18, 'attack': 3, 'armor': 0, 'effects': []},
    'Elemental':    {'hp': 15, 'attack': 4, 'armor': 0, 'effects': []},
    'Mech':         {'hp': 30, 'attack': 2, 'armor': 0, 'effects': []},
    'Pirate':       {'hp': 11, 'attack': 5, 'armor': 0, 'effects': []},
    'Quilboar':     {'hp': 21, 'attack': 2, 'armor': 0, 'effects': []}
}

def create_hero(name):
    stats = HERO_STATS.get(name)
    hero = Hero(name, stats['hp'], stats['attack'], stats['armor'], effects = [])
    hero.effects = [create_effect(effect_name, hero) for effect_name in stats['effects']]
    return hero

heroes = [create_hero(name) for name in HERO_STATS.keys()]


