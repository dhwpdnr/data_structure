class TNode():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def path_length(root):
    if root is None:
        return 0
    left = path_length(root.left)
    right = path_length(root.right)
    return max(left, right) + 1


def reverse(root):
    if root is None:
        return None
    left = reverse(root.left)
    right = reverse(root.right)
    return TNode(root.data, right, left)
