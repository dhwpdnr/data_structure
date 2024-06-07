class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def printNodes(node: ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next


class SLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):  # O(1)
        node = ListNode(val)
        node.next = self.head
        self.head = node

    # but when the list
    def addBack(self, val):  # O(n)
        node = ListNode(val)
        crnt_node = self.head
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node

    def findNode(self, val):  # O(n)
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')

    def addAfter(self, node, val):  # O(1)
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node

    def deleteAfter(self, prev_node):  # O(1)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next


# 이중 연결 리스트
class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


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
