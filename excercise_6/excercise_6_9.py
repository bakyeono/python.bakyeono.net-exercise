# 연습문제 6-9
def is_prime(number):
    """number가 소수인지 여부를 반환한다."""
    # 1은 소수가 아니다.
    if number == 1:
        return False

    # 2 이상 number 미만인 모든 수를 순회하며
    for number2 in range(2, number):
        # 그 수 가운데 number의 약수가 있는지를 검사한다.
        if number % number2 == 0:
            # 약수가 있다면 number는 소수가 아니다.
            return False

    # 약수가 하나도 없다면 number는 소수다.
    return True


# 1 이상 100 미만의 모든 소수의 합
total = 0
for number in range(1, 100):
    if is_prime(number):
        total += number
print(total)
