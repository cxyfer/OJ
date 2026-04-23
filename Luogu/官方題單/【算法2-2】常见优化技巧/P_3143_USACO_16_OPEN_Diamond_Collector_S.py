"""
P3143 [USACO16OPEN] Diamond Collector S
https://www.luogu.com.cn/problem/P3143
Greedy + Two Pointers / Binary Search

枚舉第二個區間的最小值(左端點)，並求出第二個區間的最大長度。
此時基於貪心思想，若要最大化兩個區間的長度和，則第一個區間的最大值(右端點)最好能 < 第二個區間的最小值(左端點)。
可以維護在滿足上述條件下，第一個區間的最大長度。

而在固定左端點或右端點時，能獲得的最大長度，可以用二分或雙指標來求出。
"""


def solve():
    n, k = map(int, input().split())
    A = [int(input()) for _ in range(n)]

    A.sort()

    L = [0] * n  # L[i] 表示以 i 為右端點時，最小的合法左端點
    R = [0] * n  # R[i] 表示以 i 為左端點時，最大的合法右端點

    """Binary Search"""
    # from bisect import bisect_left, bisect_right
    # for i, x in enumerate(A):
    #     L[i] = bisect_left(A, x - k)
    #     R[i] = bisect_right(A, x + k) - 1

    """Two Pointers"""
    i = 0
    for j, x in enumerate(A):
        while i < n and A[i] < x - k:
            i += 1
        L[j] = i
    j = n - 1
    for i in range(n - 1, -1, -1):
        x = A[i]
        while j >= 0 and A[j] > x + k:
            j -= 1
        R[i] = j

    # 枚舉第二個區間的最小值，根據 R[i] 可以得到第二個區間的長度
    # 此時第一個區間的右端點最好是 < i 的，這樣可以最大化兩個區間的長度和
    # 為此可以維護一個變量 c1，表示第一個區間的右端點 < i 時，第一個區間的最大長度
    ans = c1 = 0
    for i in range(n):
        c2 = R[i] - i + 1
        ans = max(ans, c1 + c2)
        c1 = max(c1, i - L[i] + 1)
    print(ans)


if __name__ == "__main__":
    solve()
