# 연습문제 5-14
# 한 주의 모든 요일
days = {'월', '화', '수', '목', '금', '토', '일'}

# 직장에 가는 요일
working_days = {'월', '화', '수', '목', '금'}

# 휴식을 취하는 요일
holidays = {'토', '일'}


def is_holiday(day):
    """요일을 입력받아 그 요일이 쉬는 날이면 True, 아니면 False를 반환한다."""
    return day in holidays


# 함수의 실행 확인
print(is_holiday('화'))
print(is_holiday('토'))
