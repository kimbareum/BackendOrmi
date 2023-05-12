# Q1.
원주율 = 3.141592
print(int(원주율))

# Q2.
# "b : 1"

# Q3.
my_name = input("이름을 입력해 주세요.")
print(f"안녕하세요. {my_name}입니다.")

# Q4.
# "c : reverse()"

# Q5.
while True:
    try:
        num = int(input("양의 정수를 입력해 주세요."))
    except:
        continue
    if num > 0:
        break


def divisor(num):
    data = []

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            data.append(i)
            data.append(num // i)

    return sorted(list(set(data)))


divisor(num)


# Q6.
def solution(l, a):
    return l.count(a)


solution(["a", "b", "c", "a", "a"], "a")


# Q7.
def solution(l):
    return sorted(l, key=lambda x: x[1], reverse=True)


solution([[10, 5], [20, 3], [30, 4], [40, 1]])


# Q8.
def solution(l):
    return list(map(lambda x: abs(x[0] - x[1]), l))


solution([[10, 5], [20, 3], [30, 4], [40, 1]])


# Q9.
def solution(s):
    return sum(map(int, s))


solution("11123")


# Q10.
def solution(s):
    return s.replace("!", "").replace(" ", "")


solution("!hello!wor     ld!     ")
