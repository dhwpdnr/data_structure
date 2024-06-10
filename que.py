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

    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1:self.rear + 1])
        else:
            return str(self.array[self.front + 1:self.capacity] + self.array[0:self.rear + 1])

    def is_empty(self):
        return self.front == self.rear  # front와 rear가 같으면 공백 상태

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front  # rear 다음이 front이면 포화 상태

    def enqueue(self, item):
        # 포화가 아니면 삽입 가능
        # rear를 시계 방향으로 회전시키고 그 위치에서 새로운 요소를 저장
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass  # 오버플로 예외

    def dequeue(self):
        if not self.is_empty():
            # 공백이 아니면 삭제 가능
            # front 를 회전시키고 그 위치의 요소 반환
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass  # 언더플로 예외

    def peek(self):
        if not self.is_empty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass  # 언더플로 예외

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity


q = CircularQueue(8)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.enqueue("F")

print("A B C D E F 삽입", q)
print("dequeue -> ", q.dequeue())
print("dequeue -> ", q.dequeue())
print("dequeue -> ", q.dequeue())
print("dequeue 3번 진행 ", q)
q.enqueue("G")
q.enqueue("H")
q.enqueue("I")
print("G H I 삽입", q)

# Queue 라이브러리 사용
import queue

data_queue = queue.Queue()

data_queue.put("abc")
data_queue.put(1)

data_queue.qsize()  # 2
data_queue.get()  # abc -> 제일 먼저 인서트된 데이터 출력

data_queue.qsize()  # 1 -> 9번줄에서 abc가 빠져나갔기 때문
data_queue.get()  # 1 출력

# LIFO Queue
lifo_queue = queue.LifoQueue()

lifo_queue.put("abc")
lifo_queue.put(1)

lifo_queue.qsize()  # 2
lifo_queue.get()  # 1 -> LIFO 구조이기 때문에 1이 먼저 출력

lifo_queue.qsize()  # 1 -> 9번줄에서 1가 빠져나갔기 때문
lifo_queue.get()  # abc 출력

# Priority Queue
priority_queue = queue.PriorityQueue()

priority_queue.put((10, "abc"))  # 우선순위를 표현하기 위해 튜플로 인서트 (우선순위, value)
priority_queue.put((5, 1))
priority_queue.put((15, "ef"))

priority_queue.qsize()  # 3 -> 데이터는 3개
priority_queue.get()  # (5,1) -> 우선순위가 가장 높은 데이터 출력

priority_queue.qsize()  # 2 -> 10번줄에서 (5,1)가 빠져나갔기 때문
priority_queue.get()  # (10,"abc") -> 두번째 우선순위
