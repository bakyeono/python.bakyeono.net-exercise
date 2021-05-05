# 연습문제 7-9
def length(sequence):
    """시퀀스 하나를 매개변수로 입력받아 요소의 개수를 반환한다."""
    result = 0
    for _ in sequence:
        result += 1
    return result


# 함수의 동작 확인
print(length([]))
print(length([1, 7, 8, 9]))
print(length(range(128)))
