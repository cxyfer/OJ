"""
D. Sequence Coloring
https://ac.nowcoder.com/acm/contest/120561/D
貪心 + 二分答案

如果 t 秒可以完成，則 t + 1 秒一定也可以完成；若 t 秒不能完成，則 t - 1 秒也不一定完成。
故答案具有單調性，可以對答案二分。

定義 nxt[i] 為從 i 開始經過 1 秒後可以到達的最遠位置，即 i + A[i]，
然而如果從 i - 1 出發可以到達更遠的位置，那麼從 i - 1 出發會更優，故可以取前綴最大值。

則如果從一個點起始點，那麼只要 T 次 i = nxt[i] 便可以求出 T 秒後可以到達的最遠位置，
直到到達所有位置 (i >= n) ，或無法更新 (i == nxt[i]) 為止。
此時若還未到達所有位置，則需要其他的起始點，檢查起始點的數量是否 <= k 即可。
"""
from itertools import accumulate

def solve() -> None:
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    if sum(1 for x in A if x > 0) <= k:
        print(0)
        return

    nxt = list(accumulate([i + x for i, x in enumerate(A)], func=max))
    def check(T: int) -> bool:
        cnt = tim = 0
        i = 0
        while i < n:
            while i < n and A[i] == 0:
                i += 1
            if i >= n:
                return True
            cnt += 1
            if cnt > k:
                return False
            tim = 0
            while i < n and tim < T and nxt[i] > i:
                i = nxt[i]
                tim += 1
            i += 1
        return True

    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left if left <= n else -1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()