# 단순 연결 노드 클래스
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


# 연결된 스택 클래스
class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def is_full(self):
        return False

    # 삽입연산
    def push(self, e):
        self.top = Node(e, self.top)

    # 삭제연산
    def pop(self):
        if not self.is_empty():
            n = self.top
            self.top = n
            return n.data

    def peek(self):
        if not self.is_empty():  # 공백이 아니면
            return self.top.data  # 머리 노드의 데이터 반환

    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def __str__(self):
        arr = []
        node = self.top
        while not node == None:
            arr.append(node.data)
            node = node.link
        return str(arr)


class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx > self.size:
            print("Overflow: Index Error")
            return None
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        if idx <= self.size // 2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail
            for _ in range(self.size - idx):
                target = target.prev
            return target

    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(value, None, self.head)
            tmp.prev = self.head
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(value, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1

    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(value)
            elif tmp == self.tail:
                self.append(value)
            else:
                tmp_prev = tmp.prev
                newNode = Node(value, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
        self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print("Underflow Error")
            return
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
            else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del (tmp)
            self.size -= 1

    def printlist(self):
        target = self.head
        while target != self.tail:
            if target.next != self.tail:
                print(target.data, '<=> ', end='')
            else:
                print(target.data)
            target = target.next
