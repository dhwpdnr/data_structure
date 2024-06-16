from que import CircularQueue


# 이진트리를 위한 노드 클래스
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# 전위순회
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)


# 중위순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)


# 후위순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


# 레벨 순회
def level_order(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


# 이진트리 노드 수 계산
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)


# 이진트리 단말 노드 수 계산
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)


# 이진트리의 높이 계산
def calc_height(n):
    if n is None:
        return 0
    h_left = calc_height(n.left)
    h_right = calc_height(n.right)
    if h_left > h_right:
        return h_left + 1
    else:
        return h_right + 1


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('\n전위순회:\t', end='')
inorder(root)
print('\n중위순회:\t', end='')
preorder(root)
print('\n후위순회:\t', end='')
postorder(root)
print('\n레벨순회:\t', end='')
level_order(root)

print('\n노드의 수:', count_node(root))
print('단말 노드의 수:', count_leaf(root))
print('트리의 높이:', calc_height(root))
print()
