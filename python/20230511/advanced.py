import json


# def writefile(func):
#     def wrap_func(a, b):
#         answer = func(a, b)
#         data = dict(zip(["a", "b", "a+b"], [a, b, answer]))
#         with open("result.txt", "w") as f:
#             json.dump(data, f, indent="\t")
#         return answer

#     return wrap_func


# @writefile
# def add(a, b):
#     return a + b

def writefile(func):
    def wrap_func(a, b):
        answer = func(a, b)
        data = locals()
        data = {i : data.get(i) for i in data if i == 'a' or i == 'b'}
        data.update({'a+b' : answer})
        with open("result.txt", "w") as f:
            json.dump(data, f, indent="\t")
        return answer

    return wrap_func


@writefile
def add(a, b):
    return a + b


print(add(2, 3))


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
