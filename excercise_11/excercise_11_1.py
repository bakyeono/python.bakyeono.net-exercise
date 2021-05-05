# 연습문제 11-1
import math


def quotient(dividend, divisor):
    """나뉨수(dividend)를 나눗수(divisor)로 나눈 몫을 계산하여 반환한다."""
    return math.floor(dividend / divisor)


def test_quotient():
    """quotient 함수를 테스트한다."""
    assert quotient(10, 3) == 3
    assert quotient(9, 5) == 1
    assert quotient(1, 99) == 0


test_quotient()
print(quotient(10, 6))
