from hero import IceMag, FireMag, TT, CT, PersianAssassin, SyiranAssassin, BlueArcher, RedArcher
from player import Player
from battlegrounds import Battlegrounds, random

bg = Battlegrounds()

heroes = [
    IceMag,
    FireMag,
    TT,
    CT,
    PersianAssassin,
    SyiranAssassin,
    BlueArcher,
    RedArcher
]

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