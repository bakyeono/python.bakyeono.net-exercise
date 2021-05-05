# 연습문제 6-8
def biggest(lst):
    """리스트 하나를 매개변수로 전달받아 리스트에서 가장 큰 요소를 반환한다."""
    # 가장 큰 요소를 저장하기 위한 변수
    biggest_element = lst[0]  # 변수의 초깃값으로 리스트의 첫번째 요소를 넣어 둔다.

    # 리스트의 첫번째 요소를 제외한 모든 요소를 순회한다.
    for element in lst[1:]:
        # 가장 큰 요소로 저장해 둔 요소보다 현재 요소가 더 크다면,
        if biggest_element < element:
            # 가장 큰 요소를 현재 요소로 바꾼다.
            biggest_element = element

    # 모든 요소를 비교했으므로, 순회가 끝나면 가장 큰 요소가 저장되어 있다.
    return biggest_element


# 함수의 동작 확인
print(biggest([4, 65, 1, 99, 40, -5, 0, 58]))
