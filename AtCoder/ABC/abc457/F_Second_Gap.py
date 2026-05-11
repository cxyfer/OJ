"""
ABC457F Second Gap
https://atcoder.jp/contests/abc457/tasks/abc457_f
DP/刷表法
定義 f[i][j] 為考慮 [i...n) 的區間，且最大值位於 j 的方案數。
那麼存在三種情況：
1. i 成為新的最大值，根據題意，此時次大值（原本的最大值）需要在 j = i + D[i]
2. i 成為新的次大值，此時最大值同樣需要在 j = i + D[i]
3. i 並非最大值也非次大值，此時原本的最大值可以在任何位置，但 D[i] 需要等於 D[i + 1]
   而 P[i] 可以是第 3...(n - i + 1) 大的值，因此可能的選擇有 n - i - 1 種

考慮轉移目標，則三種情況的轉移為
：
1. f[i][i] += f[i + 1][j]
2. f[i][j] += f[i + 1][j]
3. f[i][k] += f[i + 1][k] * (n - i - 1) for k in range(i + 1, n)
最終答案為 sum(f[0])

由於 n 可達 2e5，顯然逐個位置維護 f 值的方法肯定會超時。
因此考慮以滾動的方式將二維的 f 變成一維的。
注意到我們需要一個可以支援單點加、區間乘、單點和區間查詢的資料結構，可以使用懶標記線段樹。

但可以注意到，區間乘永遠是對後綴的區間進行操作，因此也可以只維護全局 mul 標記。
"""

from collections import defaultdict
from atcoder.lazysegtree import LazySegTree

MOD = 998244353


def solve1():
    n = int(input())
    D = list(map(int, input().split()))
    assert len(D) == n - 1

    def op(x: int, y: int) -> int:
        return (x + y) % MOD

    def mapping(f: int, x: int) -> int:
        return (f * x) % MOD

    def composition(f: int, g: int) -> int:
        return (f * g) % MOD

    f = LazySegTree(op, 0, mapping, composition, 1, n)
    f.set(n - 1, 1)
    f.set(n - 2, 1)
    for i in range(n - 3, -1, -1):
        j = i + D[i]
        fj = f.get(j)  # f[i + 1][j]

        if D[i] == D[i + 1]:
            f.apply(i + 1, n, n - i - 2)
        else:
            f.apply(0, n, 0)

        f.set(i, op(f.get(i), fj))
        f.set(j, op(f.get(j), fj))

    print(f.all_prod())


def solve2():
    n = int(input())
    D = list(map(int, input().split()))
    assert len(D) == n - 1

    f = defaultdict(int)
    f[n - 2] = f[n - 1] = 1
    mul = 1

    for i in range(n - 3, -1, -1):
        j = i + D[i]
        fj = f[j] * mul % MOD  # f[i+1][j]

        if D[i] == D[i + 1]:
            c = n - i - 2
            mul = mul * c % MOD
        else:
            f.clear()
            mul = 1
        add = fj * pow(mul, MOD - 2, MOD) % MOD
        f[i] = (f[i] + add) % MOD
        f[j] = (f[j] + add) % MOD

    ans = sum(v for v in f.values()) * mul % MOD
    print(ans)


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
