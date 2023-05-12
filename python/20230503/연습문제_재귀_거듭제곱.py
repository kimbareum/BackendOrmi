# x의 n승
def my_pow(x, n):
    if n == 0:
        return 1
    return x * my_pow(x, n-1)


# 빠른 x의 n승 (분할정복 알고리즘)
def my_pow2(num1, num2):
    if num2 == 0:
        return 1
    if num2 == 1:
        return num1
    if num2 % 2 == 0:
        half = my_pow(num1, num2 // 2)
        return half * half
    else:
        half = my_pow(num1, num2 // 2)
        return half * half * num1

print(my_pow(2,10))
print(my_pow2(2,10))