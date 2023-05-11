class Node:
    dataset = []

    def __init__(self, *data):
        self.data = list(data)
        self.next = None
        self.dataset.append(self)

node1 = Node(10,20)
node2 = Node(20,30)
node3 = Node(30,40)

for i in range(len(node1.dataset)-1):
    node1.dataset[i].next = node1.dataset[i+1]

print(node1.data, node1.next.data, node1.next.next.data)