# 연습문제 8-12
import random


class Dice:
    def __init__(self, sides):
        """인스턴스를 초기화한다."""
        self._sides = sides
        self._top = self.roll()

    def top(self):
        """주사위의 나온 면을 반환한다."""
        return self._top

    def roll(self):
        """주사위를 굴리고 나온 면을 반환한다."""
        self._top = random.randint(1, self._sides)
        return self.top()


dice_4 = Dice(4)  # 사면체 주사위 생성
print('사면체 주사위 테스트 ----')
print('처음 나온 면:', dice_4.top())
print('다시 굴리기:', dice_4.roll())
print('다시 굴리기:', dice_4.roll())

dice_100 = Dice(100)  # 백면체 주사위 생성
print('백면체 주사위 테스트 ----')
print('처음 나온 면:', dice_100.top())
print('다시 굴리기:', dice_100.roll())
print('다시 굴리기:', dice_100.roll())
