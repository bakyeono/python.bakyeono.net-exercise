# 연습문제 7-11
용의자 = [
    {'이름': '멍멍', '털': '흰색', '주둥이': '크다', '발': '크다'},
    {'이름': '킁킁', '털': '검은색', '주둥이': '작다', '발': '크다'},
    {'이름': '왈왈', '털': '흰색', '주둥이': '작다', '발': '크다'},
    {'이름': '꿀꿀', '털': '검은색', '주둥이': '작다', '발': '작다'},
    {'이름': '낑낑', '털': '흰색', '주둥이': '작다', '발': '작다'},
]

# 범인은 주둥이가 작고, 발이 크고, 흰색 털을 가진 개
profiled_dogs_1 = filter(lambda dog: dog['주둥이'] == '작다', 용의자)
profiled_dogs_2 = filter(lambda dog: dog['발'] == '크다', profiled_dogs_1)
profiled_dogs_3 = filter(lambda dog: dog['털'] == '흰색', profiled_dogs_2)

for dog in profiled_dogs_3:
    print(dog['이름'])

print([
    dog['이름']
    for dog
    in 용의자
    if dog['주둥이'] == '작다' and dog['발'] == '크다' and dog['털'] == '흰색'
])
