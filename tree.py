class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):  # 트리 생성
        self.root = None

    # 전위 순회
    def preorder(self, n):
        if n != None:
            print(n.item, '', end='')  # 노드 방문
        if n.left:
            self.preodrer(n.left)  # 왼쪽 서브 트리 순회
        if n.right:
            self.preodrer(n.right)  # 오른쪽 서브 트리 순회

    # 후위 순회
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
        if n.right:
            self.postorder(n.right)
        print(n.item, '', end='')  # 노드 방문

    # 중위 순회
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
        print(n.item, '', end='')  # 노드 방문
        if n.right:
            self.inorder(n.right)

    # 레벨 순회
    def levelorder(self, n):
        q = []
        q.append(n)
        while q:
            t = q.pop(0)
        print(t.item, '', end='')
        if t.left != None:
            q.append(t.left)
        if t.right != None:
            q.append(t.right)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

tree = BinaryTree()
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8


# 힙트리
# 힙트리는 완전 이진 트리로서, 부모 노드의 값이 자식 노드의 값보다 크거나 같은 트리이다.
# 힙트리는 최대 힙트리와 최소 힙트리로 나뉜다.
# 최대 힙트리는 부모 노드의 값이 자식 노드의 값보다 크거나 같은 완전 이진 트리이다.
# 최소 힙트리는 부모 노드의 값이 자식 노드의 값보다 작거나 같은 완전 이진 트리이다.
# 힙트리는 배열로 구현할 수 있다.
class HeapTree():
    def __init__(self):
        self.tree = [None]
        self.size = 0

    def insert(self, item):
        self.tree.append(item)
        self.size += 1
        cur = self.size
        parent = cur // 2
        while parent > 0 and self.tree[cur] > self.tree[parent]:
            self.tree[cur], self.tree[parent] = self.tree[parent], self.tree[cur]
            cur = parent
            parent = cur // 2

    def delete(self):
        if self.size == 0:
            return None
        delete_item = self.tree[1]
        self.tree[1], self.tree[self.size] = self.tree[self.size], self.tree[1]
        self.tree.pop()
        self.size -= 1
        cur = 1
        while cur * 2 <= self.size:
            child = cur * 2
            if child + 1 <= self.size and self.tree[child] < self.tree[child + 1]:
                child += 1
            if self.tree[cur] >= self.tree[child]:
                break
            self.tree[cur], self.tree[child] = self.tree[child], self.tree[cur]
            cur = child
        return delete_item

    def print_tree(self):
        print(self.tree)


heap = HeapTree()
heap.insert(3)
heap.insert(6)
heap.insert(2)
heap.insert(8)
heap.insert(1)
heap.insert(5)
heap.insert(7)
heap.insert(4)
heap.print_tree()
print(heap.delete())
heap.print_tree()
print(heap.delete())
heap.print_tree()
print(heap.delete())
heap.print_tree()
print(heap.delete())
heap.print_tree()
print(heap.delete())
heap.print_tree()
