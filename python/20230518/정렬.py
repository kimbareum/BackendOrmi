from collections import deque


def selectSort(data):
    answer = []
    while data:
        mini = min(data)
        answer.append(mini)
        data.remove(mini)
    return answer


def insertSort(data):
    data = deque(data)
    answer = [data.popleft()]
    while data:
        curr = data.popleft()
        index = len(list(filter(lambda x: x < curr, answer)))
        answer.insert(index, curr)
    return answer


def mergeSort(data):
    data_len = len(data)
    if data_len <= 1:
        return data
    mid = data_len // 2
    group1 = mergeSort(data[:mid])
    group2 = mergeSort(data[mid:])

    group = []
    while group1 and group2:
        if group1 < group2:
            group.append(group1.pop(0))
        else:
            group.append(group2.pop(0))
    group += group1 + group2
    return group


def quickSort(data):
    if len(data) <= 1:
        return data
    group1 = []
    group2 = []
    pivot = data.pop()
    for i in data:
        if i < pivot:
            group1.append(i)
        else:
            group2.append(i)
    return quickSort(group1) + [pivot] + quickSort(group2)


a = [199, 22, 33, 12, 32, 64, 72, 222, 233]
print(selectSort(a))

a = [199, 22, 33, 12, 32, 64, 72, 222, 233]
print(insertSort(a))

a = [199, 22, 33, 12, 32, 64, 72, 222, 233]
print(mergeSort(a))

a = [199, 22, 33, 12, 32, 64, 72, 222, 233]
print(quickSort(a))
