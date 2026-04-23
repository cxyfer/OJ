"""
P1886 【模板】单调队列 / 滑动窗口
https://www.luogu.com.cn/problem/P1886
Monotonic Queue
本題即 239. Sliding Window Maximum
"""

from collections import deque


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans1, ans2 = [], []
    q_mn, q_mx = deque(), deque()
    for r, x in enumerate(A):
        # 1. 入窗口，維護窗口內的最小值/最大值單調佇列
        while q_mn and A[q_mn[-1]] >= x:
            q_mn.pop()
        while q_mx and A[q_mx[-1]] <= x:
            q_mx.pop()
        q_mn.append(r)
        q_mx.append(r)
        # 2. 出窗口，移除過期元素
        while q_mn and q_mn[0] <= r - k:
            q_mn.popleft()
        while q_mx and q_mx[0] <= r - k:
            q_mx.popleft()

        # 3. 更新答案
        if r >= k - 1:
            ans1.append(A[q_mn[0]])
            ans2.append(A[q_mx[0]])

    print(*ans1)
    print(*ans2)


if __name__ == "__main__":
    solve()
