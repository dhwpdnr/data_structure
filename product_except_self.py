"""
배열이 주어졌을 때 자신을 제외한 나머지 모든 요소의 곱셈 결과를 구하라.
ex)
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
제한 조건 : 나눗셈을 사용하지 않고 O(n)에 풀이하라.
"""


def product_except_self(nums):
    out = []
    p = 1
    for i in range(0, len(nums)):
        out.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] *= p
        p *= nums[i]

    return out
