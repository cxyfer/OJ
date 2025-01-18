from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))

pos = defaultdict(int)

for i, x in enumerate(A, 1):
    if pos[str(k - x)]:
        print(pos[str(k - x)], i)
        break
    pos[str(x)] = i
else:
    print("IMPOSSIBLE")