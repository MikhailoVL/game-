import random


class Player:

    def __init__(self, name='ps'):
        self.life = 100
        self.name = name

    @property
    def vitality(self):
        return self.life

    @vitality.setter
    def vitality(self, damage):
        if self.life + damage <= 0:
            self.life = 0
        elif self.life + damage >= 100:
            self.life = 100
        else:
            self.life += damage

    def regular_damage(self):
        damage = - random.randrange(18, 26)
        print(f'\tpunch hand, {damage}')
        self.vitality = damage

    def max_damage(self):
        damage = - random.randrange(10, 36)
        print(f'\tpowerful punch leg, {damage}')
        self.vitality = damage

    def healing(self):
        heal = random.randrange(18, 26)
        print(f'\ttouch holy finger {heal}')
        self.vitality = heal

    move = {
        'regular_damage_': regular_damage,
        'max_damage_': max_damage,
        'healing_': healing,
    }

    def got_impact(self):
        if self.life < 35 :
            print('\theal increase')
            move_list = list(self.move.items())
            move_list.append(('healing_', Player.healing))
            impact = random.choice(move_list)[1]
            impact(self)
        else:
            impact = random.choice(list(self.move.items()))[1]
            impact(self)


class Game:

        def __init__(self, name):
            self.first_player = Player(name)
            self.pc_player = Player("PC")

        def battle(self):
            users = random.sample([self.first_player, self.pc_player], 2)
            while self.first_player.life > 0 and self.pc_player.life > 0:

                print(f'{users[0].name} have life {users[0].life} ,'
                      f'{users[1].name} have life {users[1].life}')
                print(f'  {users[0].name} , kick a {users[1].name}')
                users[1].got_impact()
                if users[1].life > 0:
                    print(f' {users[1].name} , kick a {users[0].name}')
                    users[0].got_impact()