# 연습문제 11-3
from datetime import date
from datetime import timedelta


def counting_age(birth_date):
    """생년월일(birth_date)를 전달받아 현재 날짜 기준의 세는 나이를 반환한다."""
    # 세는 나이는 연 차이에 1을 더해 구한다.
    return date.today().year - birth_date.year + 1


def full_age(birth_date):
    """생년월일(birth_date)를 전달받아 현재 날짜 기준의 만 나이를 반환한다."""
    today = date.today()

    # 오늘 기준으로 생일이 지났는지 확인
    is_after_birthday = timedelta(0) <= today - date(today.year, birth_date.month, birth_date.day)

    # 생일 전이면 연 차이가 만 나이이고, 생일 후이면 연 차이에서 1을 더한 것이 만 나이다.
    return today.year - birth_date.year + (1 if is_after_birthday else 0)


def test_counting_age():
    """counting_age 함수를 테스트한다."""
    assert counting_age(date(1999, 1, 1)) == 23
    assert counting_age(date(1999, 8, 8)) == 23
    assert counting_age(date(2000, 1, 1)) == 22
    assert counting_age(date(2000, 8, 8)) == 22


def test_full_age():
    """full_age 함수를 테스트한다."""
    assert full_age(date(1999, 1, 1)) == 23
    assert full_age(date(1999, 8, 8)) == 22
    assert full_age(date(2000, 1, 1)) == 22
    assert full_age(date(2000, 8, 8)) == 21


test_counting_age()
test_full_age()
