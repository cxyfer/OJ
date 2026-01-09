"""
CF2183C War Strategy
https://codeforces.com/contest/2183/problem/C

若當前有 v 個士兵，向左佔據 x 個位置：
- 若 x < v：需要消耗 x 天，大本營剩下 v 個士兵。
- 若 x >= v：需要消耗 x + (x - v) = 2x - v 天，大本營剩下 x 個士兵。
向右時同理。

枚舉向左延伸的位置數 x，計算最大可以向右延伸的位置數 y，答案為 x + y + 1。
"""
def solve():
    n, m, k = map(int, input().split())

    L = k - 1
    R = n - k

    ans = 0
    for x in range(L + 1):
        rem, v = m, 1
        rem -= x if x < v else (x + (x - 1)) 
        left = v if x < v else x
        if rem < 0:
            break
        y = rem if rem <= left else (rem + left) // 2
        ans = max(ans, x + min(y, R) + 1)
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()