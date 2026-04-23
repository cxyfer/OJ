"""
P2032 扫描
https://www.luogu.com.cn/problem/P2032
Monotonic Queue
本題即 239. Sliding Window Maximum
"""

from collections import deque


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = []
    q = deque()
    for r, x in enumerate(A):
        # 1. 入窗口，維護窗口內的最大值單調佇列
        while q and A[q[-1]] <= x:
            q.pop()
        q.append(r)
        # 2. 出窗口，移除過期元素
        while q and q[0] <= r - k:
            q.popleft()
        # 3. 更新答案
        if r >= k - 1:
            ans.append(A[q[0]])
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
