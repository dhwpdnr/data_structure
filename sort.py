# 과정 출력
def print_step(arr, val):
    print("Step %2d = ", val, end=' ')
    print(arr)


# 선택 정렬
def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if (a[j] < a[least]):
                least = j

        a[i], a[least] = a[least], a[i]
        print_step(a, i + 1)


# 삽입 정렬
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print_step(a, i)
