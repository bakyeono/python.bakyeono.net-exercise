# 연습문제 4-5
order_memo = """주문1: 아메리카노
주문2: 카페라테
주문3: 아메리카노, 아메리카노
주문4: 아메리카노, 카페라테
주문5: 카페라테, 카페라테
"""

number_of_orders = order_memo.count('주문')
cup_of_ordered_americano = order_memo.count('아메리카노')
cup_of_ordered_cafe_latte = order_memo.count('카페라테')

print('주문 받은 횟수:', number_of_orders)
print('주문받은 아메리카노의 잔 수:', cup_of_ordered_americano)
print('주문받은 카페라테의 잔 수:', cup_of_ordered_cafe_latte)
