class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def calc_height(n):
    if n is None:
        return 0
    h_left = calc_height(n.left)
    h_right = calc_height(n.right)
    if h_left > h_right:
        return h_left + 1
    else:
        return h_right + 1


# 노드의 균형 인수 계산
def calc_height_diff(n):
    if n is None:
        return 0
    return calc_height(n.left) - calc_height(n.right)


# AVL 의 LL 회전
def rotate_LL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B


# AVL 의 RR 회전
def rotate_RR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B


# AVL 의 LR 회전
def rotate_LR(A):
    B = A.left
    A.left = rotate_RR(B)
    return rotate_LL(A)


# AVL 의 RL 회전
def rotate_RL(A):
    B = A.right
    A.right = rotate_LL(B)
    return rotate_RR(A)


def insert_avl(root, node):
    if root == None:  # 공백 노드에 도달하면, 이 위치에 삽입
        return node  # node 를 반환

    if node.key == root.key:  # 동일한키 허용 안함
        return root  # root 반환

    # root 의 서브 트리에 node 삽입
    if node.key < root.key:
        root.left = insert_avl(root.left, node)
    elif node.key > root.key:
        root.right = insert_avl(root.right, node)

    bf = calc_height_diff(root)

    if bf > 1:  # 왼쪽 서브트리에서 불균형 발생 : LL, LR 회전
        if node.key < root.left.key:  # 왼쪽의 왼쪽에 삽입
            return rotate_LL(root)
        else:  # 왼쪽의 오른쪽에 삽입
            return rotate_LR(root)

    elif bf < -1:  # 오른쪽 서브트리에서 불균형 발생 : RR, RL 회전
        if node.key > root.right.key:  # 오른쪽의 오른쪽에 삽입
            return rotate_RR(root)
        else:
            return rotate_RL(root)  # 오른쪽의 왼쪽에 삽입

    return root
