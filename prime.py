"""
1부터 10000까지 소수의 합은?
"""
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = 100000
prime_list = [2]
for i in range(3, n + 1):
    if is_prime(i):
        prime_list.append(i)

print(sum(prime_list))
