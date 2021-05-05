# 연습문제 7-10
def longest(*sequences):
    """여러 개의 시퀀스를 전달받아 요소의 개수가 가장 많은 시퀀스를 반환한다."""
    winner = []
    for sequence in sequences:
        if len(winner) < len(sequence):
            winner = sequence
    return winner


# 함수의 동작 확인
print(longest([1, 2, 3], (4, 5), [], 'abcdefg', range(5)))
print(longest('파이썬', '프로그래밍'))
print(longest(range(10), range(100), range(50)))
