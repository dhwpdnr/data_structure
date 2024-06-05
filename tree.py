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
