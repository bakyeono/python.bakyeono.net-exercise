# 연습문제 4-3
def almost_equal(real_number_a, real_number_b, threshold=0.0001):
    """두 실수의 차이가 허용치(threshold) 미만인지 여부를 반환한다."""
    return abs(real_number_a - real_number_b) < threshold


print(almost_equal(0.0055, 0.00559))  # True
print(almost_equal(0.0055, 0.0056))  # False
print(almost_equal(0.0055, 0.0056, threshold=0.001))  # True
