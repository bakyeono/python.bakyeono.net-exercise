# 연습문제 5-4
def minmax(sequence):
    """전달받은 시퀀스의 최솟값과 최댓값을 리스트에 담아 반환한다."""
    return [min(sequence), max(sequence)]


# 함수의 동작 확인
print(minmax([92, -21, 0, 104, 51, 76, -92]))
print(minmax(['파', '이', '썬', '프', '로', '그', '래', '밍']))
