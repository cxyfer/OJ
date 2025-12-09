"""
CSES-2422 Multiplication Table
https://cses.fi/problemset/task/2422

第 k 大/第 k 小 => 二分查找
"""

def solve():
    n = int(input())
    m = n * n // 2 + 1

    def check(k):
        cnt = 0
        for x in range(1, n + 1):
            cnt += min(n, k // x)
        return cnt >= m

    left, right = 1, n * n
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)

if __name__ == "__main__":
    solve()