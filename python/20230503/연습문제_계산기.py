# try except 로 예외처리를 하면 문자열이나 list의 덧셈 곱셈등은 정상적으로 수행됨.
# 이 상황은 바라지 않아서 type을 확인해서 예외처리를 함.
# 에러코드등을 반환해서 코드가 멈추게 하고 싶지 않아서 inf 값을 반환해서 간접적으로 오류 발생을 알림.


def plus(num1, num2):
    if type(num1) != int and type(num1) != float or type(num2) != int and type(num2) != float:
        return float('inf')
    return num1+num2

def minus(num1, num2):
    if type(num1) != int and type(num1) != float or type(num2) != int and type(num2) != float:
        return float('inf')
    return num1-num2

def multiply(num1, num2):
    if type(num1) != int and type(num1) != float or type(num2) != int and type(num2) != float:
        return float('inf')
    return num1*num2

def divide(num1, num2):
    if type(num1) != int and type(num1) != float or type(num2) != int and type(num2) != float:
        return float('inf')
    if num2 == 0:
        return float('inf')
    return num1/num2

print(f'plus : {plus(10, 5)}')
print(f'minus : {minus(10, 5)}')
print(f'multiply : {multiply(10, 5)}')
print(f'divide : {divide(10, 5)}')
print(f'plus : {plus("10", 5)}')
print(f'minus : {minus(True, 5)}')
print(f'multiply : {multiply(10, [5])}')
print(f'divide : {divide(10, 0)}')
