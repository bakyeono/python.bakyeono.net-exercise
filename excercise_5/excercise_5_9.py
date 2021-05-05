# 연습문제 5-9
def reverse(sequence):
    """시퀀스를 입력받아 반대 순서로 뒤집어 반환한다."""
    return sequence[::-1]


# 함수의 동작 확인
print(reverse([10, 20, 30, 40]))
print(reverse(tuple('일월화수목금토')))
print(reverse(range(10)))
print(reverse('파이썬 프로그래밍'))
