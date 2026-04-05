from create_heroes import heroes
from player import Player
from battlegrounds import Battlegrounds, random

bg = Battlegrounds()

nicknames = [
    'Саня',
    'Ваня',
    'Максим',
    'Артур',
    'Денис',
    'Никита',
    'Серега',
    'Леня'
]

random.shuffle(heroes)
random.shuffle(nicknames)

for i in range(8):
    bg.add_player(Player(nicknames[i], heroes[i]))

bg.match()