# 연습문제 8-8
import math


def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x


class Coordinate:
    x = 0
    y = 0

    def distance(self, other):
        """이 Coordinate와 다른 Coordinate 사이의 거리를 반환한다."""
        return math.sqrt(square(self.x - other.x) + square(self.y - other.y))


point_1 = Coordinate()
point_1.x = -1
point_1.y = 2

point_2 = Coordinate()
point_2.x = 2
point_2.y = 3


# 클래스의 동작 확인
print(point_1.distance(point_2))
