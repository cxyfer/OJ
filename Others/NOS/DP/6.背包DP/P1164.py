"""
P1164 小A点菜
https://www.luogu.com.cn/problem/P1164
背包DP模板題，求方案數
"""
def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    f = [0] * (M + 1)
    f[0] = 1
    for x in A:
        for v in range(M, x - 1, -1):
            f[v] += f[v - x]
    print(f[M])

if __name__ == "__main__":
    solve()