class Deque:
    """덱 클래스 구현"""
    rear = 0
    front = 0
    MAX_SIZE = 100
    deq = list()

    def __init__(self):
        self.rear = 0
        self.front = 0
        self.deq = [0 for i in range(self.MAXSIZE)]

    # 덱이 비어 있는지 확인
    def is_empty(self):
        if self.rear == self.front:
            return True

        return False

    # 덱이 가득 차 있는지 확인
    def is_full(self):
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            return True
        return False

    # 맨 앞 원소 가져오기
    def get_front(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return -1
        front = (self.front + 1) % self.MAX_SIZE
        return self.deq[front]

    # 맨 뒤 원소 가져오기
    def get_rear(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return -1
        return self.deq[self.rear]

    # 뒤에서 원소 추가
    def add_rear(self, x):
        if self.is_full():
            print("ERROR: FULL")
            return
        self.rear = (self.rear + 1) % (self.MAX_SIZE)
        self.queue[self.rear] = x

    # 앞에서 원소 추가
    def add_front(self, x):
        if self.is_full():
            print("ERROR: FULL")
            return
        self.deq[self.front] = x
        self.front = (self.front - 1 + self.MAX_SIZE) % self.MAX_SIZE

    # 앞에서 원소 삭제
    def del_front(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        self.front = (self.front + 1) % self.MAX_SIZE
        return self.queue[self.front]

    # 뒤에서 원소 삭제
    def del_rear(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        tmp = self.deq[self.rear]
        self.rear = (self.rear - 1 + self.MAX_SIZE) % self.MAX_SIZE
        return tmp

    # 전체 원소 출력
    def deque_print(self):
        i = (self.front + 1) % self.MAX_SIZE
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        while i != self.rear:
            print(self.deq[i], ' ')
        i = (i + 1) % self.MAX_SIZE
        print(self.deq[i])


from que import CircularQueue


# 원형 큐를 상속한 원형 덱
class CircularDeque(CircularQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def add_front(self, item):
        if not self.is_full():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass

    def add_rear(self, item):
        self.enqueue(item)

    def delete_front(self):
        return self.dequeue()

    def delete_rear(self):
        if not self.is_empty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else:
            pass

    def get_front(self):
        return self.peek()

    def get_rear(self):
        if not self.is_empty():
            return self.array[self.rear]
        else:
            pass


# deque 모듈 사용
from collections import deque

mydeq = deque([1, 2, 3, 4])
for i in range(len(mydeq)):
    print(mydeq[i])

mydeq.appendleft(-10)  # 왼쪽에 데이터 삽입
print(mydeq)  # deque([-10, 1, 2, 3, 4])

mydeq.append(10)  # 오른쪽에 데이터 삽입
print(mydeq)

mydeq = deque([1, 2, 3, 4])

# 오른쪽에서 데이터 제거
print(mydeq.pop())  # 4
print(mydeq)  # deque([1, 2, 3])

# 왼쪽에서 데이터 제거
print(mydeq.popleft())  # 1
print(mydeq)  # deque([2, 3])
