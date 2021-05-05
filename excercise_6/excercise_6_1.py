# 연습문제 6-1
def price(number_of_products):
    """구매할 상품의 수를 입력받아 가격의 합을 계산한다.
    한꺼번에 많은 양을 구매하면 할인이 적용된다."""
    if number_of_products < 10:
        return number_of_products * 100

    elif number_of_products < 30:
        return number_of_products * 95

    elif number_of_products < 100:
        return number_of_products * 90

    else:
        return number_of_products * 85


# 함수의 동작 확인
print(price(5))
print(price(10))
print(price(15))
print(price(30))
print(price(50))
print(price(100))
