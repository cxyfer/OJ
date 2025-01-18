# Topological sort

import sys
sys.setrecursionlimit(10**9)

# Input
N = int(input())
prerequisities = [list(map(int, input().split(" ")))[1:] for _ in range(N)]

# Process
flags = [0] * N # 0: WHITE, 1: GRAY, 2: BLACK
ans = []
def dfs(i):
    if flags[i] == 2:
        return True
    if flags[i] == 1:
        return False
    flags[i] = 1
    for j in prerequisities[i]:
        if not dfs(j-1): return False
    flags[i] = 2
    ans.append(i+1)
    return True
dfs(0)
for idx in ans[:-1]:
    print(idx, end=" ")


