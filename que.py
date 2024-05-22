# Que 구현
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def insert(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node  # 현재 큐 객체의 tail에 새로운 노드 추가
        self.tail = new_node  # tail 재설정.

    def popleft(self):
        if self.is_empty():
            return 'Empty'
        new_node = self.head.next
        delete_node = self.head
        self.head = new_node
        return delete_node.value

    def top(self):
        if self.is_empty():
            return 'Empty'
        return self.head.value


q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())


# 원형 Que 구현
class CircularQueue():
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass

    def peek(self):
        if not self.is_empty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass
