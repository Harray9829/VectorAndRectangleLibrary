import math


class Vector2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.x + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.x - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.x * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.x / other)

    def magnitude_square(self):
        return self.x * self.x + self.y * self.y

    def magnitude(self):
        return math.sqrt(self.magnitude_square())

    def normalized(self):
        return self / self.magnitude()

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def to_string(self):
        return "Vector2(" + str(self.x) + ", " + str(self.y) + ")"

    def to_list(self):
        return [self.x, self.y]

