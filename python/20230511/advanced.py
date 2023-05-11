import json


def writefile(func):
    def wrap_func(a, b):
        result = func(a, b)
        data = dict(zip(["a", "b", "a+b"], [a, b, result]))
        with open("result.txt", "w") as f:
            json.dump(data, f, indent="\t")
        return result

    return wrap_func


@writefile
def add(a, b):
    return a + b


add(5, 2)


# def writefile(func):
#     def wrap_func(a, b):
#         data = dict(zip(["a", "b", "a+b"], [a, b, a + b]))
#         with open("result.txt", "w") as f:
#             json.dump(data, f, indent="\t")
#         return func(a, b)

#     return wrap_func


# @writefile
# def add(a, b):
#     return a + b

# add(4, 3)
