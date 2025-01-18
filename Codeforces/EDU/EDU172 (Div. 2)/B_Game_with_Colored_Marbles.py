from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    colors = list(input().split())
    cnt = Counter(colors)
    c1 = sum(1 for cnt in cnt.values() if cnt == 1)
    c2 = sum(1 for cnt in cnt.values() if cnt > 1)
    k = (n + 1) // 2
    h = (c1 + 1) // 2
    print(2 * h + min(c2, k - h))