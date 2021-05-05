# 연습문제 5-2
def center(sequence):
    """시퀀스를 하나 입력받아, 그 시퀀스의 가운데 요소를 반환한다.
    단, 이 함수에는 홀수 개의 요소를 가 지는 시퀀스만을 입력하기로 약속한다."""
    return sequence[len(sequence) // 2]


# 함수의 동작 확인
print(center(['가', '나', '다', '라', '마']))
print(center([2, 4, 8, 16, 32]))
