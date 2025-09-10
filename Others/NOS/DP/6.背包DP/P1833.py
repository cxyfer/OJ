"""
P1833 樱花
https://www.luogu.com.cn/problem/P1833
背包DP模板題：混合背包
"""
def solve():
    ts, te, n = input().split()
    n = int(n)
    def convert(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    T = convert(te) - convert(ts)

    # f[s] 表示花費總時間為 s 時，能獲得的最大幸福值
    f = [0] * (T + 1)
    for _ in range(n):
        t, c, p = list(map(int, input().split()))
        if p == 0:  # 完全背包
            for j in range(t, T + 1):
                f[j] = max(f[j], f[j - t] + c)
        elif p == 1:  # 01背包
            for j in range(T, t - 1, -1):
                f[j] = max(f[j], f[j - t] + c)
        else:  # 多重背包
            items = []
            s = tot = 0
            while s < p:
                x = min(s + 1, p - tot)
                tot += x
                items.append((t * x, c * x))
                s += x
            for t, c in items:
                for j in range(T, t-1, -1):
                    f[j] = max(f[j], f[j - t] + c)
    print(max(f))

if __name__ == "__main__":
    solve()