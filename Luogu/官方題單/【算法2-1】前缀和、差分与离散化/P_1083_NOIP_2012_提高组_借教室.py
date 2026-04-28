"""
P1083 [NOIP 2012 提高组] 借教室
https://www.luogu.com.cn/problem/P1083
二分 + 差分
如果能滿足前 k 個需求，則前 k - 1 個需求也能滿足；如果不能滿足第 k 個需求，則第 k + 1 個需求也不能滿足。
因此我們可以二分第幾個需求不能滿足，然後檢查是否能滿足前 mid 個需求。
"""

from array import array


def solve():
    n, m = map(int, input().split())
    A = array("l", map(int, input().split()))

    D = array("l", [])
    L = array("l", [])
    R = array("l", [])
    for _ in range(m):
        d, l, r = map(int, input().split())
        D.append(d)
        L.append(l - 1)
        R.append(r - 1)

    diff = array("l", [0] * (n + 1))

    def check(mid: int) -> bool:
        for i in range(n + 1):
            diff[i] = 0
        for i in range(mid):
            d, l, r = D[i], L[i], R[i]
            diff[l] += d
            diff[r + 1] -= d
        for i in range(1, n):
            diff[i] += diff[i - 1]
        return all(diff[i] <= A[i] for i in range(n))

    left, right = 0, m
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    # left 是第一個不能被滿足的需求
    if left <= m:
        print(-1, left, sep="\n")
    else:
        print(0)


if __name__ == "__main__":
    solve()
