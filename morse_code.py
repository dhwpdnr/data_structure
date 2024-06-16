table = [
    ("A", ".-"), ("B", "-..."), ("C", "-.-."), ("D", "-.."), ("E", "."), ("F", "..-."), ("G", "--."), ("H", "...."),
    ("I", ".."), ("J", ".---"), ("K", "-.-"), ("L", ".-.."), ("M", "--"), ("N", "-."), ("O", "---"), ("P", ".--."),
    ("Q", "--.-"), ("R", ".-."), ("S", "..."), ("T", "-"), ("U", "..-"), ("V", "...-"), ("W", ".--"), ("X", "-..-")
]


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]


def decode_slow(code):
    for e in table:
        if code == e[1]:
            return e[0]
    return None


def make_morse_tree():
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:  # 모스 코드의 각 부호에 대해
            # . 이면 왼쪽으로 진행
            if c == '.':
                if node.left is None:
                    node.left = TNode(None, None, None)
                node = node.left
            # - 이면 오른쪽으로 진행
            elif c == '-':
                if node.right is None:
                    node.right = TNode(None, None, None)
                node = node.right
        node.data = tp[0]
    return root


def decode(code, root):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data


morse_code_tree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)

print("모스 부호 : ", mlist)
print("디코드 : ", end='')

for code in mlist:
    print(decode(code, morse_code_tree), end='')
print()
