import random
import Veggie
def print_field(self):
    print("#" * (self.width * 2 + 2))
    for row in self._field:
        print("#", end="")
        for item in row:
            symbol = " " if not item else item.get_symbol()
            print(f"{symbol} ", end="")
        print("#")
    print("#" * (self.width * 2 + 2))


def get_score(self):
    return self._score


def move_rabbits(self):
    for rabbit in self._rabbits:
        move_x = random.choice([-1, 0, 1])
        move_y = random.choice([-1, 0, 1])
        x = rabbit.get_x() + move_x
        y = rabbit.get_y() + move_y

        if 0 <= x < len(self._field[0]) and 0 <= y < len(self._field):
            if isinstance(self._field[y][x], Veggie):
                self._field[rabbit.get_y()][rabbit.get_x()] = None
                rabbit.set_x(x)
                rabbit.set_y(y)
                self._field[y][x] = rabbit
                print("A rabbit ate a veggie!")
            elif not self._field[y][x]:
                self._field[rabbit.get_y()][rabbit.get_x()] = None
                rabbit.set_x(x)
                rabbit.set_y(y)
                self._field[y][x] = rabbit