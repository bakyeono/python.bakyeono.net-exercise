# 연습문제 3-2
def print_absolute():
    """사용자로부터 정수를 입력받아 그 수의 절댓값을 화면에 출력한다."""
    print('정수를 입력하세요.')
    user_number = int(input())
    print(user_number, '의 절댓값:', abs(user_number))


print_absolute()
