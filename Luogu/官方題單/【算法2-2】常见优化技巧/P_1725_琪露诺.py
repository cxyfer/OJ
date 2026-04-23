"""
P1725 琪露诺
https://www.luogu.com.cn/problem/P1725
單調佇列優化DP

令 f[i] 表示以 i 為結尾的最大得分，則轉移來源可以是 i - R ... i - L 的位置。
即 f[i] = max(f[j] + A[i] for j in range(i - R, i - L + 1))
但這個轉移需要 O(R - L + 1) 次比較，會超時。

注意到轉移來源是一個固定大小的區間，因此只要維護這個窗口的最大值即可，
這可以用滑動窗口最大值的思想，使用單調佇列優化。
"""

from collections import deque


def solve():
    n, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n + 1

    f = [0] + [float("-inf")] * n
    q = deque()
    for i, x in enumerate(A):
        # for j in range(max(0, i - R), i - L + 1):
        #     f[i] = max(f[i], f[j] + x)

        # 1. 入窗口，維護窗口內的最大值單調佇列
        if i - L >= 0:
            while q and f[q[-1]] <= f[i - L]:
                q.pop()
            q.append(i - L)
        # 2. 出窗口，移除過期元素
        while q and q[0] < i - R:
            q.popleft()
        # 3. 更新答案
        if q:
            f[i] = max(f[i], f[q[0]] + x)

    # 只有滿足 i + R > n 的 f[i] 可能為答案
    print(max(f[n - R + 1 :]))


if __name__ == "__main__":
    solve()
