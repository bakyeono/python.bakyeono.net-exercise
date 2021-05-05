# 연습문제 6-3
def is_leap_year(year):
    """연도를 입력받아 그 해가 윤년인지를 반환한다."""
    return (year % 4 == 0) and (not (year % 100 == 0)) or (year % 400 == 0)


# 날이 31개 있는 달의 집합
months_with_31_days = {1, 3, 5, 7, 8, 10, 12}

# 날이 30개 있는 달의 집합
months_with_30_days = {4, 6, 9, 11}

# 날이 28개 또는 29개 있는 달의 집합
months_with_28_or_29_days = {2}


def days_in_month(year, month):
    """연도와 월을 입력받아 그 달이 며칠까지 있는지 반환한다."""
    if month in months_with_31_days:
        return 31

    if month in months_with_30_days:
        return 30

    if month in months_with_28_or_29_days:
        return 29 if is_leap_year(year) else 28


print('2020년 2월의 날의 수:', days_in_month(2020, 2))
print('2021년 2월의 날의 수:', days_in_month(2021, 2))
print('2021년 5월의 날의 수:', days_in_month(2020, 5))
print('2021년 9월의 날의 수:', days_in_month(2020, 11))
