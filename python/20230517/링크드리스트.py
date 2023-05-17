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
        self.count = 0

    def __add__(self, added):
        self.tail.next = added.head.next

    def __mul__(self, mutiplier):
        pass

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
        self.tail.next = newNode
        self.tail = newNode
        self.count += 1

    def pop(self, index=-1):
        previousNode = self.head
        currentNode = previousNode.next
        if index == -1:
            index = self.count - 1
        for _ in range(index):
            previousNode, currentNode = currentNode, currentNode.next
        previousNode.next = currentNode.next
        self.count -= 1
        return currentNode.data

    def remove(self, target):
        currentNode = self.head
        while currentNode:
            if currentNode.next.data == target:
                currentNode.next = currentNode.next.next
                self.count -= 1
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


l = LinkedList()
l2 = LinkedList()
l.append(90)
l.append(2)
l.append(77)
l.append(35)
l.append(21)

l2.append(90)
l2.append(2)
l2.append(77)
l2.append(35)
l2.append(21)

print(l)
l + l2
print(l)
# print(l)
# print(l.find(35))

# print(l.pop(2))

# print(l)
# print(l.find(35))

# for i in l:
#     print(i)
