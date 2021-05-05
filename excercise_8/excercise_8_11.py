# 연습문제 8-11
import math


def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x


class Coordinate:
    def __init__(self, x=0, y=0):
        """인스턴스를 초기화한다."""
        self.x = x
        self.y = y

    def distance(self, other):
        """이 Coordinate와 다른 Coordinate 사이의 거리를 반환한다."""
        return math.sqrt(square(self.x - other.x) + square(self.y - other.y))


class Shape:
    def describe(self):
        """도형의 특징을 화면에 출력한다."""
        print('이 도형은', self.sides, '개의 변을 가지고 있습니다.')


class Triangle(Shape):
    sides = 3

    def __init__(self, point_a, point_b, point_c):
        """인스턴스를 초기화한다."""
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def circumference(self):
        """이 삼각형의 둘레를 반환한다."""
        side_a = self.point_a.distance(self.point_b)
        side_b = self.point_b.distance(self.point_c)
        side_c = self.point_c.distance(self.point_a)
        return side_a + side_b + side_c


class Rectangle(Shape):
    sides = 4

    def __init__(self, point_a, point_b, point_c, point_d):
        """인스턴스를 초기화한다."""
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def circumference(self):
        """이 사각형의 둘레를 반환한다."""
        side_a = self.point_a.distance(self.point_b)
        side_b = self.point_b.distance(self.point_c)
        side_c = self.point_c.distance(self.point_c)
        side_d = self.point_d.distance(self.point_a)
        return side_a + side_b + side_c + side_d


shapes = [
    Triangle(Coordinate(0, 0), Coordinate(3, 0), Coordinate(3, 4)),
    Rectangle(Coordinate(2, 2), Coordinate(6, 2), Coordinate(6, 6),
              Coordinate(2, 6)),
]
for shape in shapes:
    shape.describe()
    print('둘레:', shape.circumference())
