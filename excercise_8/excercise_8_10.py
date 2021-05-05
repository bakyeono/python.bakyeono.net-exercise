# 연습문제 8-10
class Shape:
    def describe(self):
        """도형의 특징을 화면에 출력한다."""
        print('이 도형은', self.sides, '개의 변을 가지고 있습니다.')


class Triangle(Shape):
    sides = 3


class Rectangle(Shape):
    sides = 4


shapes = [
    Triangle(),
    Rectangle(),
]
for shape in shapes:
    shape.describe()
