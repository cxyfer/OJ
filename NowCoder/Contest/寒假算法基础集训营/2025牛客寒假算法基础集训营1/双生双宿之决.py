from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    if n & 1:
        print("No")
        continue

    cnt = Counter(A)

    if len(cnt) == 2 and all(v == n // 2 for v in cnt.values()):
        print("Yes")
    else:
        print("No")