"""
P1115 最大子段和
https://www.luogu.com.cn/problem/P1115

本題有三種 O(N) 解法：
1. 前綴和(Prefix Sum) + 枚舉右維護左
   [l, r] 區間的子陣列和為 s[r] - s[l-1]，因此可以枚舉右端點 r，維護左端點 l 使得 s[r] - s[l-1] 最大
2. 動態規劃(Dynamic Programming)
   f[i] 表示以 i 為結尾的最大子陣列和，則 f[i] = max(f[i-1] + a[i], a[i])
   最後在取 max(f) 即可
3. 分治(Divide and Conquer)
   透過維護 lSum, rSum, mSum, tot 四種資訊可以做到 O(N)，用較為暴力的方式也能做到 O(N log N)
詳見 https://gdst.dev/posts/LC-53/
"""


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    # 1. 前綴和(Prefix Sum) + 枚舉右維護左
    def solve1():
        ans = float("-inf")
        s = mn = 0
        for x in A:
            s += x
            ans = max(ans, s - mn)
            mn = min(mn, s)
        return ans

    # 2. 動態規劃(Dynamic Programming)
    def solve2():
        ans = -float("inf")
        f = 0
        for x in A:
            f = max(f + x, x)
            ans = max(ans, f)
        return ans

    # 3. 分治(Divide and Conquer)
    def solve3():
        class Node:
            def __init__(self, lSum, rSum, mSum, tot):
                self.lSum = lSum
                self.rSum = rSum
                self.mSum = mSum
                self.tot = tot

        def query(l, r):
            if l == r:
                return Node(A[l], A[l], A[l], A[l])
            mid = (l + r) >> 1
            ls = query(l, mid)
            rs = query(mid + 1, r)
            lSum = max(ls.lSum, ls.tot + rs.lSum)
            rSum = max(rs.rSum, rs.tot + ls.rSum)
            mSum = max(ls.mSum, rs.mSum, ls.rSum + rs.lSum)
            tot = ls.tot + rs.tot
            return Node(lSum, rSum, mSum, tot)

        return query(0, n - 1).mSum

    # print(solve1())
    # print(solve2())
    print(solve3())


if __name__ == "__main__":
    solve()
