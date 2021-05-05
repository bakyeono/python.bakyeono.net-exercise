# 연습문제 7-14
import random


def infinity_random_generator(number_from, number_to):
    """number_from 에서 number_to 사이의 임의의 수를 무한히 생성하는 난수 생성기를 반환한다."""
    while True:
        yield random.randint(number_from, number_to)


# 함수의 동작 확인
random_numbers = infinity_random_generator(1, 20)
for i, random_number in zip(list(range(10)), random_numbers):
    print(i, '번째로 뽑은 임의의 수:', random_number)
