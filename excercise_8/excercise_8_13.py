# 연습문제 8-13
class Food:
    """음식을 나타내는 클래스"""

    def __init__(self, taste, calorie):
        """인스턴스를 초기화한다."""
        self._taste = taste  # 맛
        self._calorie = calorie  # 칼로리

    def __str__(self):
        """이 음식을 표현하는 문자열을 반환한다."""
        return str(self._taste) + '만큼 맛있고, ' + str(self._calorie) + '만큼 든든한 음식'

    def __add__(self, other):
        """이 음식(self)과 다른 음식(other)을 더한 새 음식을 반환한다."""
        taste = self._taste + other._taste
        calorie = self._calorie + other._calorie
        return Food(taste, calorie)

    def __eq__(self, other):
        """self == other 를 평가한다."""
        return self._taste == other._taste and self._calorie == other._calorie

    def __lt__(self, other):
        """self < other 를 평가한다."""
        return self._taste < other._taste if self._taste != other._taste else self._calorie < other._calorie

    def __le__(self, other):
        """self <= other 를 평가한다."""
        return self == other or self < other

    def __gt__(self, other):
        """self > other 를 평가한다."""
        return other < self

    def __ge__(self, other):
        """self >= other 를 평가한다."""
        return other <= self

    def __ne__(self, other):
        """self != other 를 평가한다."""
        return not self == other


strawberry = Food(9, 32)
potato = Food(6, 66)
sweet_potato = Food(12, 131)
pizza = Food(13, 266)
print('딸기 < 감자: ', strawberry < potato)
print('감자 + 감자 < 고구마: ', potato + potato < sweet_potato)
print('피자 >= 딸기: ', pizza >= strawberry)
print('피자 >= 피자: ', pizza >= strawberry)
print('감자 + 딸기 < 피자: ', potato + strawberry < pizza)
print('딸기 == 딸기: ', potato == potato)
