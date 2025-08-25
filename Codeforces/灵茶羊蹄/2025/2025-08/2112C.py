"""
2112C. Coloring Game
枚舉 + 相向雙指標

假設 Alice 選了 a, b, c，其中 a <= b <= c
則 Bob 有兩種選擇
1. 選剩餘的數中最大的數 d = max(S - {a, b, c})
2. 選 c

故 Alice 的選擇需滿足
1. a + b > c
2. a + b + c > d => a + b > d - c
=> a + b > max(c, d - c)

由於 d 是定值，因此可以枚舉 c，並且計算有多少 a, b 滿足條件。
"""

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i in range(2, n):  # 枚舉 c
        target = max(A[i], A[n - 1] - A[i])
        # 枚舉 b，維護 a 的範圍
        l = 0
        for r in range(i - 1, -1, -1):
            while l < r and A[l] + A[r] <= target:  # 維護 a + b > c
                l += 1
            if l >= r:
                break
            ans += r - l
    print(ans)

t = int(input())
for _ in range(t):
    solve()