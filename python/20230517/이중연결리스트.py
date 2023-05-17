class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        init = Node("init")
        self.head = init
        self.tail = init
        self.len = 0

    def __add__(self, added):
        newSelf = self.copy()
        currentNode = added.head.next
        for _ in range(added.len):
            newSelf.append(currentNode.data)
            currentNode = currentNode.next
        return newSelf

    def __mul__(self, multiplier):
        originLen = self.len
        newLinkedList = self.copy()
        for _ in range(multiplier - 1):
            currentNode = newLinkedList.head.next
            for __ in range(originLen):
                newLinkedList.append(currentNode.data)
                currentNode = currentNode.next
        return newLinkedList

    def __iter__(self):
        currentNode = self.head.next
        while currentNode:
            yield currentNode.data
            currentNode = currentNode.next

    def __str__(self):
        currentNode = self.head.next
        s = ""
        while currentNode:
            s += f"{currentNode.data}, "
            currentNode = currentNode.next
        return f"<{s[:-2]}>"

    def append(self, data):
        newNode = Node(data)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.len += 1

    def appendleft(self, data):
        newNode = Node(data)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        self.len += 1

    def extend(self, data):
        for i in data:
            self.append(i)

    def extendleft(self, data):
        for i in data:
            self.appendleft(i)

    def insert(self, index, data):
        newNode = Node(data)
        currentNode = self.head
        for _ in range(index):
            currentNode = currentNode.next
        newNode.prev = currentNode
        currentNode.next.prev = newNode
        newNode.next = currentNode.next
        currentNode.next = newNode
        self.len += 1

    def pop(self, index=-1):
        if index == -1 or index == self.len - 1:
            self.tail.prev.next = self.tail.next
            self.len -= 1
            return self.tail.data
        elif index == 0:
            currentNode = self.head.next
            self.head.next = currentNode.next
            currentNode.next.prev = self.head
            self.len -= 1
            return currentNode.data
        else:
            currentNode = self.head
            for _ in range(index + 1):
                currentNode = currentNode.next
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            self.len -= 1
            return currentNode.data

    def popleft(self):
        temp = self.head.next.data
        self.head.next = self.head.next.next
        self.head.next.next.prev = self.head
        self.len -= 1
        return temp

    def remove(self, target):
        currentNode = self.head.next
        while currentNode:
            if currentNode.data == target:
                currentNode.prev.next = currentNode.next
                self.len -= 1
                break
            currentNode = currentNode.next

    def find(self, target):
        currentNode = self.head.next
        count = 0
        while currentNode:
            if currentNode.data == target:
                return count
            currentNode = currentNode.next
            count += 1
        return -1

    def count(self, target):
        count = 0
        currentNode = self.head.next
        while currentNode:
            if currentNode.data == target:
                count += 1
            currentNode = currentNode.next
        return count

    def copy(self):
        newLinkedList = LinkedList()
        currentNode = self.head.next
        while currentNode:
            newNode = Node(currentNode.data)
            newNode.prev = newLinkedList.tail
            newLinkedList.tail.next = newNode
            newLinkedList.tail = newNode
            newLinkedList.len += 1
            currentNode = currentNode.next
        return newLinkedList

    def reverse(self):
        currentNode = self.head.next
        for i in range(self.len):
            currentNode.prev, currentNode.next = currentNode.next, currentNode.prev
            currentNode = currentNode.prev
        self.head.next, self.tail = self.tail, self.head.next
        self.tail.next = None


data = [99, 88, 77, 66, 55]
l = LinkedList()

for i in data:
    l.append(i)
print(f"append : {l}")

l.appendleft(9999)
print(f"appendleft(9999) : {l}")

l.extend([1, 2, 3, 4, 5])
print(f"extend([1,2,3,4,5]) : {l}")

l.extendleft([6, 7, 8, 9, 10])
print(f"extendleft([6, 7, 8, 9, 10]) : {l}")

l.insert(4, 7777)
print(f"insert(4,7777) : {l}")

print(f"pop() : {l.pop()}")
print(f"pop() : {l}")

print(f"pop(3) : {l.pop(3)}")
print(f"pop(3) : {l}")

print(f"l.popleft() : {l.popleft()}")
print(f"l.popleft() : {l}")

l.remove(66)
print(f"l.remove(66) : {l}")

print(f"l.find(77) :{l.find(77)}")
print(f'l.find("a") :{l.find("a")}')

l2 = l.copy()
print(f"l2 = l.copy() - l : {l}")
print(f"l2 = l.copy() - l2 : {l2}")

l2.reverse()
print(f"l2.reverse() : {l2}")

l3 = l + l2
print(f"l + l2 : {l3}")

l4 = l * 2
print(f"l4 = l3 * 2 : {l4}")

print(f"l4.count(99) : {l4.count(99)}")
