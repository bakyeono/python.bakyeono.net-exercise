# 연습문제 6-4
def calculate_bmi(height, weight):
    """키와 체중을 전달받아 체질량지수(BMI)를 계산해 반환한다."""
    return weight / (height * height)


def check_obesity(height, weight):
    """키와 체중을 전달받아 비만도 검사 결과를 반환한다."""
    bmi = calculate_bmi(height, weight)

    if bmi < 18.5:
        return '저체중'

    if bmi < 23:
        return '정상'

    if bmi < 25:
        return '과체중'

    return '비만'


print('키를 입력하세요(m):', end=' ')
height = float(input())

print('몸무게를 입력하세요(kg):', end=' ')
weight = float(input())

obesity = check_obesity(height, weight)
print(obesity, '입니다.', sep='')
