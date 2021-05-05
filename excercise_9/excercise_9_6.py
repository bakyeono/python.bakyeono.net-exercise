# 연습문제 9-6
class AccountException(Exception):
    """계좌 관련 예외"""


class AccountBalanceException(AccountException):
    """계좌 잔고 예외"""


class FrozenAccountException(AccountException):
    """동결 계좌 예외"""


class InvalidTransactionException(AccountException):
    """잘못된 입출금 예외"""


class Account:
    """은행 계좌"""
    def __init__(self, balance, is_frozen):
        """인스턴스를 초기화한다."""
        self.balance = balance  # 계좌 잔액
        self.is_frozen = is_frozen  # 계좌 동결 여부

    def check(self):
        """계좌의 잔고를 조회한다."""
        print('계좌 잔액은', self.balance, '원입니다.')

    def deposit(self, amount):
        """계좌에 amount만큼의 금액을 입금한다."""
        if amount < 0:
            raise InvalidTransactionException('거래금액이 잘못되었습니다.')

        self.balance += amount

    def withdraw(self, amount):
        """계좌에서 amount만큼의 금액을 인출한다."""
        if amount < 0:
            raise InvalidTransactionException('거래금액이 잘못되었습니다.')

        if self.balance < amount:
            raise AccountBalanceException('계좌의 잔액이 부족합니다.')

        if self.is_frozen:
            raise FrozenAccountException('계좌가 동결되었습니다.')

        self.balance -= amount


# 클래스의 동작 확인
account_1 = Account(balance=10000, is_frozen=False)

print('음수 금액 입금 시도')
try:
    account_1.deposit(-1)
except Exception as error:
    print(error)

print('음수 금액 출금 시도')
try:
    account_1.withdraw(-1)
except Exception as error:
    print(error)

print('초과 금액 출금 시도')
try:
    account_1.withdraw(20000)
except Exception as error:
    print(error)


account_2 = Account(balance=10000, is_frozen=True)

print('동결 계좌 출금 시도')
try:
    account_2.withdraw(10000)
except Exception as error:
    print(error)

account_3 = Account(balance=0, is_frozen=False)

print('정상 입금 시도')
account_3.deposit(10000)

print('정상 출금 시도')
account_3.withdraw(5000)

print(account_3.balance)
