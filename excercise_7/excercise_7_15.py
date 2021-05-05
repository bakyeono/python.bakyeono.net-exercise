# 연습문제 7-15
def input_orders(n):
    """n개의 음료를 주문받아 리스트로 반환한다."""
    return (input() for _ in range(n))


# 음료 주문 세 개를 입력받아 각 음료마다 제조 지시한다
for drink in input_orders(3):
    print(drink, '만들어 주세요!')
