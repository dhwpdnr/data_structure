"""
1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 9이라는 숫자를 모두 카운팅 해야한다.
"""


def count_8():
    count = 0
    for i in range(1, 10001):
        count += str(i).count('8')
    return count


def count_8_2():
    count = 0
    for i in range(1, 10001):
        count += len([x for x in str(i) if x == '8'])
    return count


def count_8_3():
    return sum([str(i).count('8') for i in range(1, 10001)])

