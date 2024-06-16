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


# 연결된 리스트 클래스
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def is_full(self):
        return False

    def get_node(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def get_entry(self, pos):
        node = self.get_node(pos)
        if node == None:
            return None
        else:
            return node.data

    def insert(self, pos, elem):
        before = self.get_node(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            before.link = Node(elem, before.link)

    def delete(self, pos):
        before = self.get_node(pos - 1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link


# 연결된 큐 클래스
class LinkedQueue:
    def __init__(self):
        self.tail = None

    def is_empty(self):
        return self.tail == None

    def is_full(self):
        return False

    def enqueue(self, item):
        node = Node(item, None)
        if self.is_empty():
            self.tail = node
            node.link = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.is_empty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count

    def __str__(self):
        arr = []
        if not self.is_empty():
            node = self.tail.link
            while not node == self.tail:
                arr.append(node.data)
                node = node.link
            arr.append(node.data)
        return str(arr)


# 이중 연결 구조의 노드 클래스
class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


# 연결된 덱 클래스

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def is_full(self):
        return False

    def add_front(self, item):
        node = DNode(item, None, self.front)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def add_rear(self, item):
        node = DNode(item, self.rear, None)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def delete_front(self):
        if not self.is_empty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def delete_rear(self):
        if not self.is_empty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data
