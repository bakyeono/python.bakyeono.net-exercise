# 연습문제 5-5
def mean(sequence):
    """시퀀스를 하나 입력받아 시퀀스 내 모든 요소의 산술평균을 반환한다."""
    return sum(sequence) / len(sequence)


# 함수의 동작 확인
print(mean([92, -21, 0, 104, 51, 76, -92]))
