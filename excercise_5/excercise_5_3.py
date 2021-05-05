# 연습문제 5-3
def mirror(sequence):
    """시퀀스를 하나 입력받아 그 시퀀스를 뒤집은 시퀀스를 원본에 덧붙여 반환한다.
    단, 원본 시퀀스의 마지막 요소는 덧붙이지 않는다."""
    reversed_sequence = sequence[-2::-1]
    return sequence + reversed_sequence


# 함수의 동작 확인
print(mirror([1, 2, 3]))
print(mirror([2, 4, 8, 16, 32]))
