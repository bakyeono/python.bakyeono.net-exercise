# 연습문제 9-5
class AccountException(Exception):
    """계좌 관련 예외"""


class AccountBalanceException(AccountException):
    """계좌 잔고 예외"""


class FrozenAccountException(AccountException):
    """동결 계좌 예외"""


class InvalidTransactionException(AccountException):
    """잘못된 입출금 예외"""


