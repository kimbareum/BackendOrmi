from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        # self.child = [] # 이진트리가 아니거나 그래프인 경우
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
        self.count = 1

    def __len__(self):
        return self.count

    def remove(self, target):
        currentNode = self.root
        parentNode = self.root
        while currentNode:
            if currentNode.data == target:
                break
            elif target < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left
            elif target > currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.right
        else:
            return
        # 자식노드 X
        if not currentNode.left and not currentNode.right:
            if target < parentNode.data:
                parentNode.left = None
            else:
                parentNode.right = None

        # 왼쪽 자식노드만
        elif currentNode.left and not currentNode.right:
            if target < parentNode.data:
                parentNode.left = currentNode.left
            else:
                parentNode.right = currentNode.left

        # 오른쪽 자식노드만
        elif not currentNode.left and currentNode.right:
            if target < parentNode.data:
                parentNode.left = currentNode.right
            else:
                parentNode.right = currentNode.right

        # 자식노드가 모두 있음.
        else:
            newParentNode = currentNode
            newCurrentNode = currentNode.right
            prev = newParentNode.left
            while newCurrentNode.left and newCurrentNode.right:
                newCurrentNode.left, prev = prev, newCurrentNode.left
                newCurrentNode = newCurrentNode.right
            else:
                if not newCurrentNode.left:
                    newCurrentNode.left = prev
                else:
                    while newCurrentNode:
                        if data < currentNode.data:
                            if not currentNode.left:
                                currentNode.left = prev
                                self.count += 1
                                return
                            else:
                                currentNode = currentNode.left
                        elif data > currentNode.data:
                            if not currentNode.right:
                                currentNode.right = prev
                                self.count += 1
                                return
                            else:
                                currentNode = currentNode.right
            if target < parentNode.data:
                parentNode.left = currentNode.right
            else:
                parentNode.right = currentNode.right

    def insert(self, data):
        newNode = Node(data)
        currentNode = self.root
        while currentNode:
            if data == currentNode.data:
                return
            elif data < currentNode.data:
                if not currentNode.left:
                    currentNode.left = newNode
                    self.count += 1
                    return
                else:
                    currentNode = currentNode.left
            elif data > currentNode.data:
                if not currentNode.right:
                    currentNode.right = newNode
                    self.count += 1
                    return
                else:
                    currentNode = currentNode.right

    def DFS(self):
        result = []
        stack = [self.root]
        while stack:
            currentNode = stack.pop()
            if currentNode.right:
                stack.append(currentNode.right)
            if currentNode.left:
                stack.append(currentNode.left)
            result.append(currentNode.data)
        return result

    def BFS(self):
        result = []
        queue = deque([self.root])
        while queue:
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            result.append(currentNode.data)
        return result


tree = BinaryTree(5)

tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(9)
tree.insert(11)
tree.insert(7)
tree.insert(2)
tree.insert(10)

print(tree.DFS())
tree.remove(8)
print(tree.DFS())
