def draw_tree(row, left, right):
    mid = (left + right) // 2
    if (left <= right and row < rows):
        map[row][mid] = 1
        draw_tree(row + 1, left, mid - 1)
        draw_tree(row + 1, mid + 1, right)


def printTree():
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 0:
                print('-', end='')
            else:
                print('X', end='')
        print()


rows = 6
cols = 64
map = [[0 for x in range(cols)] for x in range(rows)]
draw_tree(0, 0, cols - 1)
printTree()
