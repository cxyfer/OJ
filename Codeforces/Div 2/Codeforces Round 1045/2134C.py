"""
2134C - Even Larger
https://codeforces.com/contest/2134/problem/C
貪心

只需要使長度為 2 和 3 的子陣列滿足條件即可，
在考慮長度為 3 的子陣列時，若左右相加大於當前值，由於左側的條件已經滿足，優先操作右側的值
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, n, 2):
        if A[i] < A[i - 1]:
            ans += A[i - 1] - A[i]
            A[i - 1] = A[i]
        if i + 1 < n:
            if A[i] < A[i + 1]:
                ans += A[i + 1] - A[i]
                A[i + 1] = A[i]
            if A[i] < A[i - 1] + A[i + 1]:
                d = A[i - 1] + A[i + 1] - A[i]
                ans += d
                # 優先減少右側的值，但只能減少到 0
                if d <= A[i + 1]:
                    A[i + 1] -= d
                else:
                    d -= A[i + 1]
                    A[i + 1] = 0
                    A[i - 1] -= d
    print(ans)

t = int(input())
for _ in range(t):
    solve()