# 연습문제 9-4
print('첫 번째 수를 입력하시오: ', end='')
number1 = int(input())
print('두 번째 수를 입력하시오: ', end='')
number2 = int(input())

add = number1 + number2
subtract = number1 - number2
multiply = number1 * number2
try:
    divide = number1 / number2
except ZeroDivisionError:
    divide = None

print(number1, '+', number2, '=', add)
print(number1, '-', number2, '=', subtract)
print(number1, '*', number2, '=', multiply)
print(number1, '/', number2, '=', divide)
