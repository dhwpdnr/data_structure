# 이진 탐색 트리 노드 클래스
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


# 이진탐색트리의 탐색 연산(순환 구조)
def search_bst(n, key):
    if n is None:
        return None
    if key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)


# 이진탐색트리의 탐색 연산(반복 구조)
def search_bst_iter(n, key):
    while n is not None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None


# 이진탐색트리의 값을 이용한 탐색연산
def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)


# 최대 키 노드 찾기
def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n


# 최소 키 노드 찾기
def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n


# 이진탐색트리의 삽입 연산
def insert_bst(root, node):
    if root == None:
        return node

    if node.key == root.key:
        return root

    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    return root


# 이진탐색트리의 삭제 연산
def delete_bst(root, key):
    if root == None:
        return root

    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left

        succ = search_min_bst(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    return root


def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)


# 이진탐색트리를 이용한 맵
class BSTMap():
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def find_max(self):
        return search_max_bst(self.root)

    def find_min(self):
        return search_min_bst(self.root)

    def search_value(self, value):
        return search_value_bst(self.root, value)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        self.root = insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BSTMap : '):
        print(msg, end='')
        inorder(self.root)
        print()
