# 연습문제 7-6
def plus_elements(sequence_a, sequence_b):
    """두 개의 시퀀스를 전달받은 후 각 요소를 순서대로 합한 리스트를 반환한다."""
    new_list = []
    for element_a, element_b in zip(sequence_a, sequence_b):
        new_list.append(element_a + element_b)
    return new_list


# 함수의 동작 확인
print(plus_elements((1, 2, 3), [4, 5, 6]))
