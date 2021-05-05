# 연습문제 11-2
import re


not_hangul_pattern = r'[^가-힣]'


def hangul_only(string):
    """문자열(string)에서 한글만 골라 반환한다."""
    return re.sub(not_hangul_pattern, '', string)


def test_hangul_only():
    """hangul_only 함수를 테스트한다."""
    assert hangul_only('') == ''
    assert hangul_only('안녕') == '안녕'
    assert hangul_only('hello') == ''
    assert hangul_only('abcd 가나다라 1234') == '가나다라'


test_hangul_only()
print(hangul_only('I like 파이썬 programming.'))
print(hangul_only('a1가b2나c3다d4라e5마f6바g7사'))
