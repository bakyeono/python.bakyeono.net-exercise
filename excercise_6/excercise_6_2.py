# 연습문제 6-2
def is_leap_year(year):
    """연도를 입력받아 그 해가 윤년인지를 반환한다."""
    # - 그해의 수가 4로 나누어 떨어지면 윤년이다. 따라서 1996년은 윤년이다.
    if year % 4 == 0:
        # - 단, 그해의 수가 100로 나누어 떨어지면 윤년이 아니다. 따라서 1900년은 윤년이 아니다.
        if year % 100 == 0:
            # - 단, 그해의 수가 400으로 나누어 떨어지면 윤년이다. 따라서 2000년은 윤년이다.
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# 함수의 동작 확인
print('1996년은 윤년인가?', is_leap_year(1996))
print('1900년은 윤년인가?', is_leap_year(1900))
print('2000년은 윤년인가?', is_leap_year(2000))
print('2020년은 윤년인가?', is_leap_year(2020))
print('2021년은 윤년인가?', is_leap_year(2021))
