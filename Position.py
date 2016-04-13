import math


class Position:
    epsilon = 0.1
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Position(self.x * other, self.y * other)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return Position(abs(self.x), abs(self.y))

    def round(self):
        return Position(round(self.x), round(self.y))

    def is_almost_rounded(self):
        return abs(self.x - round(self.x)) <= Position.epsilon and \
                    abs(self.y - round(self.y)) <= Position.epsilon

    def is_almost_at(self, n):
        return abs(self.x - n.x) < Position.epsilon and abs(self.y - n.y) < Position.epsilon

    def is_in_area(self, p1, p2):
        return p1.x <= self.x <= p2.x and p1.y >= self.y >= p2.y


