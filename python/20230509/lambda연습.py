숫자 = [1, 2, 3, 4, 5]
승수 = [2, 2, 2, 3, 3]

숫자_승수 = list(zip(숫자, 승수))
제곱 = list(map(lambda x: x[0] ** x[1], 숫자_승수))
백이상 = list(filter(lambda x: x >= 100, 제곱))
제곱합 = sum(제곱)

print(f"{숫자_승수}\n{제곱}\n{백이상}\n{제곱합}")
