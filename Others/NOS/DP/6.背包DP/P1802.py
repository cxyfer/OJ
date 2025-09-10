"""
P1802 5 倍经验日
https://www.luogu.com.cn/problem/P1802
背包DP模板題：分組背包

比較直覺的作法是計算勝利相比失敗多獲得的經驗值，然後轉換為01背包問題。
但也可以看為有 n 組，每組有 2 個物品的分組背包。
因為有代價為 0 的轉移，所以需要同時從兩種狀態轉移，否則會出錯。
"""
def solve():
    n, x = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    ans = sum(a for a, _, _ in A)
    f = [0] * (x + 1)
    for a, b, w in A:
        v = b - a
        for j in range(x, w - 1, -1):
            f[j] = max(f[j], f[j - w] + v)
    print((ans + f[x]) * 5)
    # f = [0] * (x + 1)
    # for a, b, w in A:
    #     for j in range(x, -1, -1):
    #         if j >= w:
    #             f[j] = max(f[j - w] + b, f[j] + a)
    #         else:
    #             f[j] = f[j] + a
    # print(f[x] * 5)

if __name__ == "__main__":
    solve()