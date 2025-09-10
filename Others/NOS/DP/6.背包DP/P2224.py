"""
P2224 [HNOI2001] 产品加工
https://www.luogu.com.cn/problem/P2224
背包DP：將其中一維視為 weight，另一維視為 value

Python TLE, C++ AC
"""
MAX_T = int(3e4 + 5)

def solve():
    n = int(input())
    items = [list(map(int, input().split())) for _ in range(n)]

    # f[s] 表示第一台機器工作 s 時間時，第二台機器的最小工作時間
    f = [float('inf')] * MAX_T
    s = f[0] = 0
    for a, b, c in items:
        s += max(a, c)
        for t1 in range(s, -1, -1):
            t2 = float('inf')
            if a > 0 and t1 - a >= 0:
                t2 = min(t2, f[t1 - a])
            if b > 0:
                t2 = min(t2, f[t1] + b)
            if c > 0 and t1 - c >= 0:
                t2 = min(t2, f[t1 - c] + c)
            f[t1] = t2
    print(min(max(t1, t2) for t1, t2 in enumerate(f)))

if __name__ == "__main__":
    solve()