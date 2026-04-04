import random
from player import Player

class Battlegrounds:

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def match(self):
        tab = []
        rounds = 0
        random.shuffle(self.players)
        while len(self.players) > 1:
            rounds +=1
            for i in range(0, len(self.players)-1, 2):
                p1 = self.players[i]
                p2 = self.players[i+1]
                p1.attack(p2)
                if p2.hero.hp == 0:
                    tab.append(p2)
                p2.attack(p1)
                if p1.hero.hp == 0:
                    tab.append(p1)
            alive_players = [p for p in self.players if p.hero.hp > 0]
            self.players = alive_players
        tab = list(reversed(tab))
        if len(self.players) == 1:
            print('1 место:', tab[0].nickname, 'с героем', tab[0].hero.name, '\n2 место:', tab[1].nickname, 'с героем', tab[1].hero.name, '\n3 место:', tab[2].nickname, 'с героем', tab[2].hero.name)
            print('Игра шла', rounds, 'раундов')
        if len(self.players) == 0:
            print('Все игроки погибли. Победителя нет.')