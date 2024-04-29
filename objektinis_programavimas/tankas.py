import random


class Tankas:
    def __init__(self, tank_coordinates: list, target_coordinates: list, direction):
        self.tank_coordinates = tank_coordinates
        self.target_coordinates = target_coordinates
        self.direction = direction
        self.shoots = 0
        self.points = 100
        self.on_target = 0

    def print_table(self):
        for y in range(10, 0, -1):
            for x in range(10):
                if x == self.tank_coordinates[0] - 1 and y == self.tank_coordinates[1]:
                    print(tank1.direction, end='')
                elif x == self.target_coordinates[0] - 1 and y == self.target_coordinates[1]:
                    print('0', end='')
                else:
                    print('_', end='')
            print()

    def input_value(self):
        text = """
        Vaziuokite i siaure '^'
        Vaziuokite i pietus 'v'
        Vaziuokite i rytus '>'
        Vaziuokite i vakarus '<'
        Saukite 's'
        Gaukite informacija 'i'
        Atspauzdinti lentele 'p'
        :
        """
        legal_symbols = ['^', 'v', '>', '<', 's', 'i', 'p']
        player_move = input(text)
        if player_move not in legal_symbols:
            print('Tokio simbolio ivesti negalima')
        elif player_move == 's':
            self.tank_shoot()
            # shoots += 1
        elif player_move == 'i':
            self.info()
        elif player_move == 'p':
            self.print_table()
        else:
            self.direction = player_move
        return player_move

    def info(self):
        print(f'Jus turite {self.points} tasku \nTankas siuo metu pasisukes i {self.direction} '
              f'\nTanko koordinates {self.tank_coordinates} '
              f'\nTankas atliko {self.shoots} suviu \nTankas pataite {self.on_target} '
              f'\nTaikinio koortinate {self.target_coordinates}')

    def target_hit(self):
        print('Pataikete')
        self.get_target()
        self.points += 50
        self.on_target += 1
        print(self.points)
        print(self.target_coordinates)

    def tank_shoot(self):
        self.shoots += 1
        if (self.direction == '^' and int(self.tank_coordinates[1]) < int(self.target_coordinates[1])
                and self.tank_coordinates[0] == self.target_coordinates[0]):
            # print('Pataikete')
            self.target_hit()
        elif (self.direction == 'v' and int(self.tank_coordinates[1]) > int(self.target_coordinates[1])
              and self.tank_coordinates[0] == self.target_coordinates[0]):
            # print('Pataikete')
            self.target_hit()
        elif (self.direction == '<' and int(self.tank_coordinates[0]) > int(self.target_coordinates[0])
              and self.tank_coordinates[1] == self.target_coordinates[1]):
            # print('Pataikete')
            self.target_hit()
        elif (self.direction == '>' and int(self.tank_coordinates[0]) < int(self.target_coordinates[0])
              and self.tank_coordinates[1] == self.target_coordinates[1]):
            # print('Pataikete')
            self.target_hit()
        else:
            print('Pro sali')
            self.points -= 20

    def get_target(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        self.target_coordinates = [a, b]

    def tank_movement(self):
        while self.points > 0:
            player_move = self.input_value()
            x = self.tank_coordinates[0]
            y = self.tank_coordinates[1]
            if player_move == 'v':
                y = self.tank_coordinates[1] - 1
                self.points -= 10
            if player_move == '^':
                y = self.tank_coordinates[1] + 1
                self.points -= 10
            if player_move == '<':
                x = self.tank_coordinates[0] - 1
                self.points -= 10
            if player_move == '>':
                x = self.tank_coordinates[0] + 1
                self.points -= 10
            if x < 1 or x > 10 or y < 1 or y > 10 or [x, y] == self.target_coordinates:
                print('Toks judejimas negalimas, tankas uz ribu arba uzvaziavo ant taikinio')
            else:
                self.tank_coordinates = [x, y]
        self.info()


tank1 = Tankas([5, 7], [8, 7], '>')

# tank1.print_table()
# tank1.input_value()
# print(tank1.direction)
# print(tank1.shoots)
# tank1.info()
# tank1.tank_shoot()
tank1.tank_movement()
# tank1.target_hit()
