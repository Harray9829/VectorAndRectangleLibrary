
import math
from Vector2 import Vector2


class Rectangle:
    __x = 0.0
    __y = 0.0
    __w = 100.0
    __h = 100.0

    def __init__(self, x: float, y: float, w: float, h: float):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, v):
        self.__y = v

    @property
    def width(self):
        return self.__w

    @width.setter
    def width(self, v):
        self.__w = v

    @property
    def height(self):
        return self.__h

    @height.setter
    def height(self, v):
        self.__h = v

    @property
    def x1(self):
        return self.__x + self.__w

    @x1.setter
    def x1(self, v):
        self.__w = v - self.__x

    @property
    def y1(self):
        return self.__y + self.__h

    @y1.setter
    def y1(self, v):
        self.__h = v - self.__y

    @property
    def top_left(self):
        return Vector2(self.__x, self.__y)

    @top_left.setter
    def top_left(self, v: Vector2):
        self.__x = v.x
        self.__y = v.y

    @property
    def top(self):
        return Vector2(self.__x + self.__w / 2, self.__y)

    @top.setter
    def top(self, v: Vector2):
        self.__x = v.x - self.__w / 2
        self.__y = v.y

    @property
    def top_right(self):
        return Vector2(self.__x + self.__w, self.__y)

    @top_right.setter
    def top_right(self, v: Vector2):
        self.__x = v.x - self.__w
        self.__y = v.y

    @property
    def left(self):
        return Vector2(self.__x, self.__y + self.__h / 2)

    @left.setter
    def left(self, v: Vector2):
        self.__x = v.x
        self.__y = v.y - self.__h / 2

    @property
    def center(self):
        return Vector2(self.__x + self.__w / 2, self.__y + self.__h / 2)

    @center.setter
    def center(self, v: Vector2):
        self.__x = v.x - self.__w / 2
        self.__y = v.y - self.__h / 2

    @property
    def right(self):
        return Vector2(self.__x + self.__w, self.__y + self.__h / 2)

    @right.setter
    def right(self, v: Vector2):
        self.__x = v.x - self.__w
        self.__y = v.y - self.__h / 2

    @property
    def bottom_left(self):
        return Vector2(self.__x, self.__y + self.__h)

    @bottom_left.setter
    def bottom_left(self, v: Vector2):
        self.__x = v.x
        self.__y = v.y - self.__h

    @property
    def bottom(self):
        return Vector2(self.__x + self.__w / 2, self.__y + self.__h)

    @bottom.setter
    def bottom(self, v: Vector2):
        self.__x = v.x - self.__w / 2
        self.__y = v.y - self.__h

    @property
    def bottom_right(self):
        return Vector2(self.__x + self.__w, self.__y + self.__h)

    @bottom_right.setter
    def bottom_right(self, v: Vector2):
        self.__x = v.x - self.__w
        self.__y = v.y - self.__h

    def is_point_inside(self, v: Vector2):
        c1 = c2 = False
        if self.x1 > self.x:
            c1 = self.x <= v.x <= self.x1
        elif self.x1 < self.x:
            c1 = self.x1 <= v.x <= self.x
        if self.y1 > self.y:
            c2 = self.y <= v.y <= self.y1
        elif self.y1 < self.y:
            c2 = self.y1 <= v.y <= self.y

        return c1 and c2

    def is_rect_inside(self, rectangle):
        c1 = self.is_point_inside(rectangle.top_left)
        c2 = self.is_point_inside(rectangle.bottom_right)
        return c1 and c2

    def is_rect_over(self, rectangle):
        c1 = self.is_point_inside(rectangle.top_left)
        c2 = self.is_point_inside(rectangle.top_right)
        c3 = self.is_point_inside(rectangle.bottom_left)
        c4 = self.is_point_inside(rectangle.bottom_right)
        return c1 or c2 or c3 or c4
