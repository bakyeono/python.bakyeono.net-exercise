# 연습문제 8-9
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


point_1 = Coordinate(-1, 2)
point_2 = Coordinate(y=3, x=2)
point_3 = Coordinate()
point_4 = Coordinate(10)

# 클래스의 동작 확인
print((point_1.x, point_1.y))
print((point_2.x, point_2.y))
print((point_3.x, point_3.y))
print((point_4.x, point_4.y))
print(point_1.distance(point_2))
