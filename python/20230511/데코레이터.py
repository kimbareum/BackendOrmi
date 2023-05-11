data = ["10", 1, 2, 3, "20"]


def 전처리(func):
    def wrap_func(data):
        print("hello")
        return func(map(int, data))

    return wrap_func


@전처리
def sum_value(data):
    return sum(data)


print(sum_value(data))


######################################
# 이런식으로 작동됨
######################################


def wrap_func(data):
    def sum_value(data):
        return sum(data)

    print("hello")
    return sum_value(map(int, data))


print(wrap_func(data))
