# 연습문제 6-5
def absolute_number(number):
    """number의 절댓값을 반환한다."""
    return number if 0 <= number else - number


# 함수의 동작 확인
print(absolute_number(-1))
print(absolute_number(0))
print(absolute_number(1))
