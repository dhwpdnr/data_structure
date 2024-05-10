def is_palindrome(s):
    import re

    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())

    stack = []

    n = len(cleaned)

    mid = n // 2

    for i in range(mid):
        stack.append(cleaned[i])

    if n % 2 != 0:
        mid += 1

    for i in range(mid, n):
        if stack.pop() != cleaned[i]:
            return False

    return True


test_strings = ["eye", "madam, I'm Adam", "race car", "hello"]
for s in test_strings:
    print(f"'{s} 는 회문이다.")
