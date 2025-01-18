"""
根據條件 1 ，這個樹會是根節點 0 連接若干個子樹，每個子樹都是一條鏈
根據條件 2 ，這個樹會依照 Level-order 的順序編號
根據條件 3 ，節點 1 的子樹大小至少為 2

由於節點 1 一定有恰好 1 個子節點，所以可以利用條件 2，找到節點 1 的子節點
- 若 query(1, u) == 1，表示 1 和 u 會經過根節點 0，所以 u 是 0 的另一個子節點
- 若 query(1, u) == 0，表示 1 和 u 不會經過根節點 0，所以 u 是 1 的子節點

之後對於 queue 中的每個節點，都會有兩種情況
- 若 query(q[0], u) == 0，表示 u 是 q[0] 的子節點
- 若 query(q[0], u) == 1，表示 u 不是 q[0] 的子節點，且 q[0] 不會再有其他子節點
"""

from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def query(x, y):
    print(f"? {x} {y}", flush=True)
    return int(input())

def answer(A):
    print("!", *A, flush=True)

t = int(input())
for _ in range(t):
    n = int(input())
    fa = [0] * n
    fa[1] = 0

    q = deque([1])
    u = 2
    # 先找到 1 的子節點，過程中的其他節點都會是 1 的兄弟節點
    while u < n and q[0] == 1:
        if query(1, u) == 1:
            fa[u] = 0
        else:
            fa[u] = 1
            q.popleft()
        q.append(u)
        u += 1

    # Level-order Traversal
    while u < n:
        if query(q[0], u) == 0:
            fa[u] = q[0]
            q.append(u)
            u += 1
        q.popleft()

    answer(fa[1:])