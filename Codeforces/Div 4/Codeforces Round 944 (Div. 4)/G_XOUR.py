"""
    a XOR b < 4 代表除了最低的兩位以外，其他位數都相同
    把能交換的數字分成一組，然後排序，再依序填入原本的位置
"""
from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    pos = defaultdict(list)
    val = defaultdict(list)

    for i, Ai in enumerate(A):
        pos[str(Ai >> 2)].append(i) # 避免 hash collision
        val[str(Ai >> 2)].append(Ai) # 避免 hash collision

    ans = [0] * n
    for k in pos:
        for i, v in zip(pos[k], sorted(val[k])):
            ans[i] = v
    print(*ans)