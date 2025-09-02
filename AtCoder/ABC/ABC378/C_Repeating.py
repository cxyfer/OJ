"""
    紀錄每個數字最後出現的位置，如果當前數字已經出現過，則輸出最後出現的位置
    否則，則輸出 -1
"""
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

ans = [-1] * N
pos = defaultdict(lambda: -1)
for i, x in enumerate(A):
    ans[i] = pos[x]
    pos[x] = i + 1

print(*ans)