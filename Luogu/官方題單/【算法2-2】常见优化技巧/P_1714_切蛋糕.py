"""
P1714 切蛋糕
https://www.luogu.com.cn/problem/P1714
Prefix Sum + Sliding Window + Monotonic Queue

本題是在 P1115 最大子段和 或 53. Maximum Subarray 的基礎上，加上了區間大小的限制。
因此同樣可以對前綴和陣列枚舉右維護左，但左端點滿足區間大小不超過 k 的條件。
這可以用 Sliding Window + Monotonic Queue 實現。

注意更新順序，由於不允許空區間，因此在考慮右端點 r 時，可能的左端點最多只有到 r - 1，需要在更新答案後才能入隊。
"""

from collections import deque
from itertools import accumulate


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = float("-inf")
    q = deque()
    s = list(accumulate(A, initial=0))
    for r, x in enumerate(s):
        # 1. 移除過期元素
        while q and q[0] <= r - k - 1:
            q.popleft()
        # 2. 更新答案
        if q:
            ans = max(ans, x - s[q[0]])
        # 3. 入隊
        while q and s[q[-1]] >= x:
            q.pop()
        q.append(r)
    print(ans)


if __name__ == "__main__":
    solve()
