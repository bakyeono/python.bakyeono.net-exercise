# 연습문제 6-6
# 합계를 저장하는 변수
total = 0

# 5의 배수를 구하는 변수
number = 100  # 초깃값은 100
while number < 10000:  # 변수가 10000 미만인 동안에만 반복 실행한다.
    total += number  # 합계에 변수의 현재 값(5의 배수)을 더한다.
    number += 5  # 변수의 값을 5 증가한다.

print(total)
