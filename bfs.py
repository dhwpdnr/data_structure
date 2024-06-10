from que import CircularQueue

map = [
    ["1", "1", "1", "1", "1", "1"],
    ["e", "0", "1", "0", "0", "1"],
    ["1", "0", "0", "0", "1", "1"],
    ["1", "0", "1", "0", "1", "1"],
    ["1", "0", "1", "0", "0", "x"],
    ["1", "1", "1", "1", "1", "1"]
]
MAZE_SIZE = 6

que = CircularQueue()
que.enqueue((1, 0))
print("BFS: ")

# 환형 큐로 구현한 BFS
while not que.is_empty():
    cur = que.dequeue()
    row = cur[0]
    col = cur[1]
    print("(", row, ",", col, ")")

    if map[row][col] == "x":
        print("미로 탐색 성공")
        break

    map[row][col] = "."
    if row - 1 >= 0 and map[row - 1][col] == "0":
        que.enqueue((row - 1, col))
    if row + 1 < MAZE_SIZE and map[row + 1][col] == "0":
        que.enqueue((row + 1, col))
    if col - 1 >= 0 and map[row][col - 1] == "0":
        que.enqueue((row, col - 1))
    if col + 1 < MAZE_SIZE and map[row][col + 1] == "0":
        que.enqueue((row, col + 1))
    print("큐: ", que)
    print()
