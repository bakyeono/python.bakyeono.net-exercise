# 연습문제 8-7
import math


def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x


def distance(point_a, point_b):
    """두 Coordinate 사이의 거리를 반환한다."""
    return math.sqrt(square(point_a.x - point_b.x) + square(point_a.y - point_b.y))


class Coordinate:
    x = 0
    y = 0


point_1 = Coordinate()
point_1.x = -1
point_1.y = 2

point_2 = Coordinate()
point_2.x = 2
point_2.y = 3


# 함수의 동작 확인
print(distance(point_1, point_2))
