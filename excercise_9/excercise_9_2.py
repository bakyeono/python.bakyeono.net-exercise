# 연습문제 9-2
def 삼육구(n):
    """n에 숫자 '3', '6', '9' 중 하나 이상이 있을 경우 '짝'을,
        그렇지 않으면 n에 대응하는 숫자를 반환한다."""
    characters = str(n)
    found_3 = characters.find('3') != -1
    found_6 = characters.find('6') != -1
    found_9 = characters.find('9') != -1
    if found_3 or found_6 or found_9:
        return '짝'
    else:
        return str(n)


def test_삼육구():
    """삼육구 함수를 테스트한다."""
    if not(삼육구(3) == '짝'):
        return False

    if not(삼육구(6) == '짝'):
        return False

    if not(삼육구(9) == '짝'):
        return False

    if not(삼육구(300) == '짝'):
        return False

    if not(삼육구(1245786) == '짝'):
        return False

    if not(삼육구(5559555) == '짝'):
        return False

    if not(삼육구(1) == '1'):
        return False

    if not(삼육구(2) == '2'):
        return False

    if not(삼육구(128888775) == '128888775'):
        return False

    if not(삼육구(0) == '0'):
        return False

    if not(삼육구(-13) == '짝'):
        return False

    if not(삼육구(-20) == '-20'):
        return False

    if not(삼육구(-999) == '짝'):
        return False

    return True


print(test_삼육구())
