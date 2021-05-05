# 연습문제 2-8
# 식재료의 칼로리 (kcal / g)
flour_kcal_per_g = 364 / 100  # 밀가루의 칼로리
piment_kcal_per_g = 20.1 / 100  # 피망의 칼로리
olive_kcal_per_g = 115 / 100  # 올리브의 칼로리
pork_kcal_per_g = 242.1 / 100  # 돼지고기의 칼로리
cheese_kcal_per_g = 402.5 / 100  # 치즈의 칼로리

# 피자 한 판에 들어 있는 식재료의 양 (g)
pizza_flour_g = 200  # 피자에 든 밀가루의 양 (g)
pizza_piment_g = 30  # 피자에 든 피망의 양 (g)
pizza_olive_g = 10  # 피자에 든 올리브의 양 (g)
pizza_pork_g = 80  # 피자에 든 돼지고기의 양 (g)
pizza_cheese_g = 20  # 피자에 든 치즈의 양 (g)

# 피자 한 판의 칼로리
pizza_kcal = (
    pizza_flour_g * flour_kcal_per_g
    + pizza_piment_g * piment_kcal_per_g
    + pizza_olive_g * olive_kcal_per_g
    + pizza_pork_g * pork_kcal_per_g
    + pizza_cheese_g * cheese_kcal_per_g
)

# 피자를 자른 조각의 수
number_of_slices = 6

# 피자 한 조각의 칼로리
pizza_kcal_per_slice = pizza_kcal / number_of_slices

print(pizza_kcal_per_slice)
