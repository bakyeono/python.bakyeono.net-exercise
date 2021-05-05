# 연습문제 5-20
def concatenate(*strings, separator):
    """여러 개의 문자열을 연결해 반환한다. 문자열을 연결할 때 구분자를 각 문자열 사이에 끼워 넣는다."""
    return separator.join(strings)


# 함수의 동작 확인
print(concatenate('가난하다고', '해서', '외로움을', '모르겠는가', separator='/'))
print(concatenate(*'월화수목금토일', separator=' - '))
