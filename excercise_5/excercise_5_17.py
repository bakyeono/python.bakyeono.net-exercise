# 연습문제 5-17
# 0 이상 1000 미만인 3의 배수의 집합
multiple_of_3 = set(range(0, 1000, 3))

# 0 이상 1000 미만인 4의 배수의 집합
multiple_of_4 = set(range(0, 1000, 4))

# 3의 배수 집합에서 4의 배수 집합을 뺀 차집합 원소의 개수 확인
print(len(multiple_of_3 - multiple_of_4))
